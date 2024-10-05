import os
# import streamlit as st
from streamlit_chat import message
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api_key = os.getenv("GOOGLE_API_KEY")

# if not api_key:
#     st.error("GOOGLE_API_KEY not found. Please set it in your .env file or environment variables.")
#     st.stop()

genai.configure(api_key=api_key)

def get_conversational_chain():
    prompt_template = """
    You are an expert virtual assistant for the Department of Justice (DoJ) under the Ministry of Law & Justice, Government of India. Your role is to assist users in obtaining information about various aspects of the DoJ, including but not limited to:

    Details about the different divisions of the DoJ.
    Number of judges appointed across the Supreme Court, High Courts, District, and Subordinate Courts, as well as current vacancies.
    Pendency of cases through the National Judicial Data Grid (NJDG).
    Procedures for paying fines related to traffic violations.
    Live streaming of court cases.
    Steps for eFiling and ePay.
    Information about Fast Track Special Courts, including their operations.
    How to download and use the eCourts Services Mobile app.
    Accessing Tele Law Services.
    Current status of ongoing cases.
    Provide clear, step-by-step instructions and detailed explanations for each query. Include any relevant links or resources if available, and ensure to address user inquiries in a straightforward manner. If the information requested is beyond your scope or if there are updates needed, advise users to consult the DoJ website or contact relevant authorities directly.

    
    Do not reference the PDF, try to be as helpful as possible and break everything down into small simple steps for beginners.
    Provide the response in a format that can be directly used in a React application. Use valid HTML tags like <p> for paragraphs, <a> for links, <h1>/<h2> for headings, and <ul>/<li> for lists. Avoid markdown or other non-HTML formatting.
    Respond in {language}.

    Context: {context}
    Question: {question}

    Answer:
    """

    try:
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",
                                       temperature=0.3)
        prompt = PromptTemplate(template=prompt_template,
                                input_variables=["context", "question", "language"])
        chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
        return chain
    except Exception as e:
        # st.error(f"Error creating conversational chain: {str(e)}")
        return None



def question(question, language):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001")

        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(question)

        chain = get_conversational_chain()
        if chain:
            response = chain(
                {"input_documents": docs, "question": question, "language": language}, return_only_outputs=True)
            return response['output_text']
        else:
            return "Sorry, I'm having trouble generating a response. Please try again later."
    except Exception as e:
        # st.error(f"Error answering question: {str(e)}")
        return "I encountered an error while trying to answer your question. Please try again or check your setup."



# def main():
#     # st.set_page_config(page_title="Judiciary Assistance System", page_icon="🚜", layout="wide")
    
#     # st.title("🚜 Judiciary Assistance System")
#     # st.subheader("Your AI assistant for judiciary information and details")

#     # Language selection dropdown
#     languages = {
#         "English": "English",
#         "Hindi": "Hindi",
#         "Hinglish": "Hinglish",
#         "Gujarati": "Gujarati",
#         "Urdu": "Urdu",
#         "Punjabi": "Punjabi"
#     }
#     selected_language = st.selectbox("Select Language", list(languages.keys()), index=0)

#     # Initialize chat history
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display chat messages from history on app rerun
#     for i, chat in enumerate(st.session_state.messages):
#         message(chat["content"], is_user=chat["is_user"], key=str(i))

#     # React to user input
#     if prompt := st.chat_input(f"Ask about judiciary system in {selected_language}:"):
#         # Display user message in chat message container
#         st.chat_message("user").write(prompt)
#         # Add user message to chat history
#         st.session_state.messages.append({"content": prompt, "is_user": True})

#         with st.spinner("Thinking..."):
#             response = ask_question(prompt, languages[selected_language])
        
#         # Display assistant response in chat message container
#         with st.chat_message("assistant"):
#             st.write(response)
#         # Add assistant response to chat history
#         st.session_state.messages.append({"content": response, "is_user": False})

#     # Sidebar with additional information
#     with st.sidebar:
#         st.subheader("About")
#         st.write("This AI assistant is designed to help with judiciary system. Feel free to ask any questions about pending cases, judiciary procedures")
        
#         st.subheader("Need More Help?")
#         st.info("If you need further assistance, consider contacting your local judicial office or the judiciary support line.")
@app.route('/ask_question', methods=['POST'])
@cross_origin()
def ask_question():
    req_data = request.get_json()

    user_question = req_data['question']
    user_language = req_data['language']
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    response = question(user_question, user_language)
    return jsonify({"answer": response}), 200
    
if __name__ == "__main__":
    # main()
    app.run(debug=True, host="0.0.0.0")

