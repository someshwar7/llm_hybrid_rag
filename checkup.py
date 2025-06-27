import chromadb
from sentence_transformers import SentenceTransformer

# Initialize Chroma client and collection
client = chromadb.PersistentClient(path="./chroma_db")  # persistence
collection = client.get_or_create_collection("resume_collection")

# Load sentence embedding model
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Resume split into chunks for better retrieval granularity
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

# Generate unique IDs for each chunk
ids = [f"chunk_{i}" for i in range(len(resume_chunks))]

# Function to populate vector DB
def populate_resume_db():
    embeddings = embedder.encode(resume_chunks).tolist()
    collection.upsert(documents=resume_chunks, embeddings=embeddings, ids=ids)
    print("✅ Resume loaded into vector DB!")

# Function to perform basic retrieval
def query_vector_db(query, n_results=3):
    query_embedding = embedder.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return "\n".join(results["documents"][0]) if results["documents"] else "No matching info found."

# Function to debug and inspect retrieval results
def debug_query(query, n_results=3):
    query_embedding = embedder.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)

    if not results["documents"]:
        print("❌ No documents found.")
        return

    print(f"\n🔍 Query: '{query}'")
    for i, (doc, dist) in enumerate(zip(results["documents"][0], results["distances"][0])):
        print(f"\nResult {i+1}:")
        print(f"📏 Distance: {dist:.4f}")
        print(f"📄 Content: {doc}")

# Example usage
if __name__ == "__main__":
    populate_resume_db()
    query = "What are Someshwar's skills?"
    print("\n📌 Top result:\n", query_vector_db(query))
    debug_query(query)
