import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("GOOGLE_API_KEY not found. Please set it in your .env file or environment variables.")
    exit(1)

genai.configure(api_key=api_key)

def get_pdf_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {str(e)}")
        return ""

def get_text_chunks(text):
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=10000, chunk_overlap=1000)
        chunks = splitter.split_text(text)
        return chunks
    except Exception as e:
        print(f"Error splitting text: {str(e)}")
        return []

def get_vector_store(chunks):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001")
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        return True
    except Exception as e:
        print(f"Error creating vector store: {str(e)}")
        return False

def process_pdf(pdf_path):
    print(f"Processing PDF: {pdf_path}")
    raw_text = get_pdf_text(pdf_path)
    if not raw_text:
        print("No text extracted from PDF. Please check the file.")
        return

    print("Splitting text into chunks...")
    text_chunks = get_text_chunks(raw_text)
    if not text_chunks:
        print("Failed to split text into chunks.")
        return

    print("Creating vector store...")
    if get_vector_store(text_chunks):
        print("PDF processing complete. Knowledge base updated.")
    else:
        print("Failed to update knowledge base.")

def main():
    while True:
        pdf_path = input("Enter the path to the PDF file (or 'q' to quit): ").strip()
        
        if pdf_path.lower() == 'q':
            print("Exiting the program.")
            break

        if not os.path.exists(pdf_path):
            print(f"File not found: {pdf_path}")
            continue

        process_pdf(pdf_path)

        another = input("Do you want to process another PDF? (y/n): ").strip().lower()
        if another != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    print("Welcome to the Farming Equipment Manual Uploader!")
    print("This program will process PDF manuals and update the knowledge base.")
    main()