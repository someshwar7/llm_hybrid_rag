import chromadb
from sentence_transformers import SentenceTransformer

# 1️⃣ Initialize persistent Chroma client
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("resume_collection")

# 2️⃣ Load embedder
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 3️⃣ Your resume chunks
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

# 4️⃣ IDs for the chunks
ids = [f"chunk_{i}" for i in range(len(resume_chunks))]

# 5️⃣ Populate DB
def populate_resume_db():
    embeddings = embedder.encode(resume_chunks).tolist()
    collection.upsert(documents=resume_chunks, embeddings=embeddings, ids=ids)
    print("✅ Resume loaded into vector DB!")

# 6️⃣ Query DB
def query_vector_db(query, n_results=3):
    query_embedding = embedder.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    if results and "documents" in results and results["documents"]:
        return "\n".join(results["documents"][0])
    return "No matching info found."

# 7️⃣ DEBUG + TEST
if __name__ == "__main__":
    populate_resume_db()
    query = "What are Someshwar's skills?"
    print("\n🔍 Querying:", query)
    answer = query_vector_db(query)
    print("\n📌 Retrieved:\n", answer)
