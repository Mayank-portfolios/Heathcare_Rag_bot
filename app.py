import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings



st.title("Health RAG Chatbot")

@st.cache_resource
def load_vectorstore():
    loader = PyPDFLoader(r"C:\Users\mayan\OneDrive\Desktop\health care_rag based chatbot\pdf_loader\ilovepdf_merged.pdf")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(docs, embeddings)

vector_store = load_vectorstore()

model = ChatOpenAI(model="gpt-4o-mini")

user_query = st.text_input("Ask your question:")

if st.button("Search") and user_query:
    docs = vector_store.similarity_search(user_query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer only from the context below.
    If not found, say you cannot find it.

    Context:
    {context}

    Question:
    {user_query}

    Answer:
    """

    with st.spinner("Generating answer..."):
        response = model.invoke(prompt)

    st.write(response.content)