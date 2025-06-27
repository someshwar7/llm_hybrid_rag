def route_query(user_input):
    info_keywords = ["who", "what", "when", "where", "capital", "population", "define"]
    if any(kw in user_input.lower() for kw in info_keywords):
        return "RAG"
    elif "code" in user_input.lower() or "function" in user_input.lower():
        return "MODEL:CODELAMA"
    elif "resume" in user_input.lower() or "someshwar" in user_input.lower():
        return "RAG"
    else:
        return "MODEL:MISTRAL"
