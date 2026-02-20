# Heathcare_Rag_bot
🩺 Health Care RAG-based Chatbot

This project is a Retrieval-Augmented Generation (RAG) chatbot that answers health-related questions using uploaded PDFs as a knowledge base. It is built using Python, LangChain, OpenAI, ChromaDB, and Streamlit.

🚀 Features
Search and retrieve relevant information from large PDF documents.
Answer user queries intelligently using a context-aware AI model.
User-friendly web interface built with Streamlit.
Embeddings and vector database (Chroma) used for efficient similarity search.

🛠 Technologies Used
Python 3.x
Streamlit – Web app interface
LangChain – For building RAG pipeline
OpenAI GPT-3.5/GPT-4 – Language model for generating answers
ChromaDB – Vector database for similarity search
PyPDFLoader – To load PDF content
dotenv – Manage environment variables securely

📁 Project Structure
health-rag-chatbot/
│
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignore env, cache, API keys
├── pdf_loader/             # Folder containing PDF files
│     └── ilovepdf_merged.pdf

How to run
cd health-rag-chatbot
Install dependencies:
pip install -r requirements.txt
Create a .env file and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here
Run the Streamlit app:
streamlit run app.py
Open the link provided by Streamlit in your browser.

🧩 How it Works
PDFs are loaded using PyPDFLoader.
Text is split into smaller chunks for embeddings.
OpenAI embeddings convert chunks into vectors.
ChromaDB stores vectors for similarity search.
User query → similarity search → context → AI model generates answer.

📝 Learnings
Built a full RAG pipeline for question-answering.
Learned integration of vector databases with LLMs.
Streamlit development for interactive AI apps.
Handling large PDFs efficiently for search & retrieval.
Managing environment variables and API keys securely.



📌 Future Improvements

Add multiple PDF upload support.

Include chatbot memory for conversation context.

Deploy on Streamlit Cloud or Heroku for public access.
