def simple_router_logic(user_input):
    user_input_lower = user_input.lower()

    if any(op in user_input for op in ['+', '-', '*', '/']):
        return "TOOL:calculator"
    if "code" in user_input_lower or "function" in user_input_lower:
        return "MODEL:CODELAMA"
    if "who" in user_input_lower or "what" in user_input_lower or "where" in user_input_lower:
        return "RAG"
    if "story" in user_input_lower or "write" in user_input_lower:
        return "MODEL:MISTRAL"

    return "MODEL:MISTRAL"
