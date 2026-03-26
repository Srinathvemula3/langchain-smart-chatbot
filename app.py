import streamlit as st
import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# UI
st.set_page_config(page_title="Smart Chatbot", page_icon="🤖")
st.title("🤖 Smart Chatbot (RAG + LLM)")

# 🔄 Reset button
if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.session_state.vectorstore = None
    st.success("Chat reset successfully!")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# File uploader
uploaded_file = st.file_uploader("Upload PDF or TXT")

if uploaded_file:
    # Reset previous vectorstore
    st.session_state.vectorstore = None

    with open("temp_file", "wb") as f:
        f.write(uploaded_file.read())

    # Load document
    if uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader("temp_file")
    else:
        loader = TextLoader("temp_file")

    docs = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(docs)

    # Embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # Vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)
    st.session_state.vectorstore = vectorstore

    st.success("✅ Document uploaded & processed!")

    # Summary
    llm = ChatOpenAI(openai_api_key=api_key)
    summary = llm.invoke("Summarize this:\n" + docs[0].page_content)

    st.subheader("📄 Summary")
    st.write(summary.content)

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    llm = ChatOpenAI(openai_api_key=api_key)

    # 🔥 SMART LOGIC
    if st.session_state.vectorstore:
        retriever = st.session_state.vectorstore.as_retriever()

        qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever
        )

        doc_response = qa.run(f"""
        Answer ONLY if answer is clearly in the document.
        If not, say EXACTLY: NOT_FOUND

        Question: {prompt}
        """)

        if "NOT_FOUND" in doc_response:
            # Fallback to LLM
            response = llm.invoke(f"""
            Answer this question clearly using general knowledge:

            {prompt}
            """).content
        else:
            response = doc_response

    else:
        # No document → LLM answer
        response = llm.invoke(f"""
        Answer this question clearly:

        {prompt}
        """).content

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )