Here is a detailed README for your **JudiciaryAI** project that leverages React, Flask, and Gemini to create a chatbot for the judicial system of India:

---

# JudiciaryAI

**JudiciaryAI** is a chatbot built to assist in the judicial system of India by providing quick and relevant answers from legal documents such as judgments, orders, and other important legal content. The system is powered by **React** for the frontend, **Flask** for the backend, and **Google Gemini** for AI-based NLP processing. It utilizes PDF vectorization to train the model on legal documents, enabling it to understand and respond intelligently to queries.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
    1. [Backend Setup](#backend-setup)
    2. [Frontend Setup](#frontend-setup)
4. [Environment Variables](#environment-variables)
5. [Running the Project](#running-the-project)
6. [Conclusion](#conclusion)

---

## Project Overview

JudiciaryAI is designed to simplify the legal research process by providing an AI-powered assistant that can read, understand, and retrieve information from legal documents. The system involves:

- **Backend**: Flask-based server that handles PDF vectorization and communicates with the Gemini AI API to process legal data.
- **Frontend**: React application that allows users to interact with the chatbot.
- **Gemini AI**: A powerful AI model that provides the NLP capabilities needed for understanding complex legal documents.

---

## Technologies Used

- **Frontend**: React.js
- **Backend**: Flask (Python)
- **AI Model**: Google Gemini API (for NLP and machine learning)
- **PDF Processing**: Vectorization of legal PDFs to train the model
- **Database**: (Optional) You can use a database to store processed data if required.
- **Version Control**: Git/GitHub

---

## Setup Instructions

Follow these steps to set up the project locally.

### 1. Backend Setup

#### Step 1: Create Virtual Environment

1. Open VS Code and press `Ctrl + Shift + P` to open the command palette.
2. Select **"Select Python Interpreter"** and choose **"Create Virtual Environment"**.
3. Choose the required Python version.
4. Select the **bot/requirements** to install all necessary dependencies for the backend.

#### Step 2: Install Dependencies

Navigate to the **bot** directory and install the required Python dependencies:

```bash
cd bot
pip install -r requirements.txt
```

#### Step 3: Set API Key

Create a `.env` file in the **bot** directory and add your Google Gemini API key:

```bash
GOOGLE_API_KEY=<your-gemini-api-key>
```

> Replace `<your-gemini-api-key>` with your actual API key for the Google Gemini API.

#### Step 4: Load PDFs

1. In the **bot** directory, open a terminal and run:

   ```bash
   python add_pdfs.py
   ```

2. Follow the instructions in the terminal to load and vectorize the PDFs that will be used to train the model.

#### Step 5: Start Flask Server

In the same terminal, run the following command to start the Flask backend server:

```bash
python app.py
```

**Important:** Do **NOT** close this terminal. The Flask server must remain running for the chatbot to function.

---

### 2. Frontend Setup

#### Step 1: Install Dependencies

Open a new terminal window and navigate to the **front** directory:

```bash
cd front
```

Install all the necessary dependencies for the React frontend:

```bash
npm install
```

#### Step 2: Start React Development Server

Start the React development server by running:

```bash
npm start
```

This will start the frontend at [http://localhost:3001](http://localhost:3001).

---

## Environment Variables

Ensure that the following environment variables are set:

1. **GOOGLE_API_KEY**: The API key for Google Gemini, set in the `.env` file located in the **bot** directory.

---

## Running the Project

Once the backend and frontend are set up and running, follow these steps:

1. **Backend**:
   - In the **bot** directory, run `python app.py` to start the Flask server.
   - Ensure that your environment variables are correctly configured (especially the `GOOGLE_API_KEY`).

2. **Frontend**:
   - In the **front** directory, run `npm start` to launch the React app.

3. Navigate to [http://localhost:3001](http://localhost:3001) in your browser to interact with the JudiciaryAI chatbot.

---

## Conclusion

After following these steps, both the backend and frontend of the JudiciaryAI system will be running. You can now interact with the chatbot, which uses AI to understand and answer queries about the judicial system of India based on the legal documents you provide. This project offers a powerful tool for legal professionals and the general public to quickly access important legal information.

---

Feel free to contribute, raise issues, or request new features. Enjoy using JudiciaryAI!

