from rag.rag_handler import add_documents_to_vector_db
docs = [
    "Berlin is the capital of Germany.",
    "The population of Germany is over 83 million.",
    "Python is a popular programming language."
]
ids = ["1", "2", "3"]
add_documents_to_vector_db(docs, ids)
