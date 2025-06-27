def handle_tool_call(route, user_input):
    tool = route.split(":")[1]
    if tool == "calculator":
        try:
            # Safe eval without builtins
            result = eval(user_input, {"__builtins__": {}})
            return f"[Calculator] Result: {result}"
        except Exception as e:
            return f"[Calculator Error] {str(e)}"
    return f"[Tool {tool}] Not implemented yet."
