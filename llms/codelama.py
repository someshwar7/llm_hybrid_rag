import subprocess
import requests
import os

def query_codelama(user_input):
    """
    This function checks an ENV variable to decide:
    - LOCAL: use subprocess to run ollama directly.
    - REMOTE: use Cloudflare tunnel with requests.
    """
    # If you want to force remote mode, set OLLAMA_MODE=REMOTE in your environment
    mode = os.getenv("OLLAMA_MODE", "LOCAL").upper()

    if mode == "REMOTE":
        response = requests.post(
            "https://show-had-engineers-fact.trycloudflare.com/api/generate",
            json={
                "model": "codellama",
                "prompt": user_input
            }
        )
        response.raise_for_status()
        return response.json()["response"]

    else:
        result = subprocess.run(
            ["ollama", "run", "codellama", user_input],
            capture_output=True, text=True, check=True, encoding='utf-8', errors='replace'
        )
        return result.stdout
