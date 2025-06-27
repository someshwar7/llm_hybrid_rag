import subprocess

def query_mistral(user_input):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", user_input],
            capture_output=True, text=True, check=True, encoding='utf-8', errors='replace'
        )
        return f"[Mistral]\n{result.stdout.strip()}"
    except subprocess.CalledProcessError as e:
        return f"[Mistral Error] {e.stderr.strip()}"
