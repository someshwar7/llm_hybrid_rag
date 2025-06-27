# 🚀 Hybrid LLM Router with ChromaDB

This project is a **Retrieval-Augmented Generation (RAG)** pipeline that:

* Stores your resume in a **ChromaDB** vector database.
* Retrieves relevant chunks using **Sentence Transformers**.
* Routes the retrieved context to an **LLM** (local or cloud).

---

## 📂 Project Structure

```bash
.
├── chroma_db/         # Persistent ChromaDB storage  
├── llms/              # LLM handlers and models  
├── rag/               # RAG logic (retrieval, context management)  
├── response/          # Response templates/handlers  
├── router/            # Router logic to manage query flow  
├── tools/             # Utility tools (e.g., TTS, image processing)  
├── utils/             # Common utilities (helper functions etc.)  
├── checkup.py         # Loads and queries resume into ChromaDB for testing  
├── main.py            # Main script to run the hybrid LLM + RAG pipeline  
├── saperate.py        # (Optional) Additional script (maybe testing/separation logic)  
└── __init__.py        # Init file for module compatibility
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/someshwar7/hybrid_llm_rag.git
cd hybrid_llm_rag
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```txt
chromadb
sentence-transformers
openai
```

### 3. Load the resume into the vector DB

```bash
python checkup.py
```

This will populate the `chroma_db/` directory and test retrieval.

---

## 🚀 Running the Main Pipeline

```bash
python main.py
```

* Accepts natural language questions.
* Fetches context from ChromaDB.
* Passes it to the LLM for an answer.

---

## 🎥 Demo Video

[![Watch the video](https://img.shields.io/badge/Watch-Demo%20Video-blue)](https://github.com/someshwar7/hybrid_llm_rag)

---

## 🔬 Sample Query

**Prompt:**

```
What are Someshwar's skills?
```

**Top results from vector DB:**

```
- Skills: Someshwar V is skilled in Python, Java, NumPy, Pandas, Scikit-learn, TensorFlow, Keras, OpenCV, Streamlit, LangChain, MySQL, FAISS, DeepSeek, ML, DL, Computer Vision, NLP
```

---

## 📓 License

[MIT](LICENSE) — Free to use and distribute.

---

## 👤 Author

**Someshwar V**
📧 [somesh1812004@gmail.com](mailto:somesh1812004@gmail.com)
💼 [LinkedIn](https://linkedin.com/in/someshwar-v-56a0b7256)
🐈 [GitHub](https://github.com/someshwar7)

---

## ✅ Debug Tips

* Re-run `checkup.py` to debug ChromaDB.
* Make sure your embeddings match the model (e.g. MiniLM).
* Use `print()` statements in `main.py` to trace the flow.
