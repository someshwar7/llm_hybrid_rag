from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedder
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Your resume chunks
resume_chunks = [
    "Someshwar V, email: somesh1812004@gmail.com, phone: +91-9789720388, LinkedIn: linkedin.com/in/someshwar-v-56a0b7256, GitHub: github.com/someshwar7",
    "Education: B.E. in Computer Science and Engineering (2022-Present) at St. Joseph’s College of Engineering, Chennai. HSC 85.6%, SSLC 92.2%",
    "Skills: Python, Java, NumPy, Pandas, Scikit-learn, TensorFlow, Keras, OpenCV, Streamlit, LangChain, MySQL, FAISS, DeepSeek, ML, DL, Computer Vision, NLP",
    "Work Experience: Intern at MyBuildSpace, Kochi (Sept 2024-Jan 2025) - Computer Vision project, team collaboration.",
    "Deep Learning Intern at C-DAC (June-July 2024): CNNs, LSTMs, heart disease prediction, movie recommendation system.",
    "Skills: Someshwar V is skilled in Python, Java, NumPy, Pandas, Scikit-learn, TensorFlow, Keras, OpenCV, Streamlit, LangChain, MySQL, FAISS, DeepSeek, ML, DL, Computer Vision, NLP",
    "Projects: Legal Query Assistant - RAG model using DeepSeek + LangChain + FAISS, Sports Analytics - Football player/ball detection (YOLOv8, OpenCV, Streamlit).",
    "Certifications: NPTEL Data Science for Engineers, DBMS; Coursera: Intro to Data Science, Probability/Statistics; Udemy: Streamlit ML deployment."
]

# Create embeddings
embeddings = embedder.encode(resume_chunks).astype(np.float32)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Store chunks
chunks = resume_chunks

def query_vector_db(query, k=3):
    query_embedding = embedder.encode([query]).astype(np.float32)
    D, I = index.search(query_embedding, k)
    results = [chunks[i] for i in I[0]]
    return "\n".join(results)

# DEBUG
if __name__ == "__main__":
    print("✅ FAISS index ready")
    test_query = "What are Someshwar's skills?"
    print("Query:", test_query)
    print(query_vector_db(test_query))
