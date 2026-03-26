#  Smart Web Chatbot

A hybrid AI chatbot built using **LangChain, Geminiai, and Streamlit** that can answer questions from uploaded documents (PDF/TXT) and also provide general knowledge using LLM fallback.

---

## 🚀 Features

* 📄 **Document Q&A (RAG)**
  Upload PDF or TXT files and ask questions based on the content.

* 🧠 **LLM Fallback**
  If the answer is not found in the document, the chatbot uses general knowledge to respond.

* 🔍 **Semantic Search with FAISS**
  Uses vector embeddings for accurate context retrieval.

* 💬 **Chat Interface**
  Interactive chat UI using Streamlit.

* 🔄 **Reset Chat Option**
  Clears chat history and document memory.

---

## 🧠 Tech Stack

* Python
* Streamlit
* LangChain
* OpenAI API
* FAISS (Vector Database)
* Python-dotenv

---

## ⚙️ How It Works

1. Upload a document (PDF/TXT)
2. Text is split into chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User asks a question:

   * If answer exists → retrieved from document
   * Else → answered using LLM (fallback)

---

## 📁 Project Structure

```
smart-chatbot/
│── app.py
│── requirements.txt
│── .env
│── venv/
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd smart-chatbot
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

---

### 3️⃣ Activate virtual environment

**Windows:**

```
venv\Scripts\activate
```

---

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Add API Key

Create a `.env` file and add:

```
OPENAI_API_KEY=your_openai_api_key
```

---

### 6️⃣ Run the app

```
streamlit run app.py
```

---

## 🧪 Example Use Cases

* Resume analysis chatbot
* Document-based Q&A system
* Knowledge assistant
* AI-powered learning tool

---

## 💡 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* LLM Prompt Engineering
* Session State Management

---
---

## 🚀 Future Improvements

* Multi-document support
* Chat memory (context awareness)
* Real-time web search integration
* Deployment (Streamlit Cloud / AWS)

---
---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
