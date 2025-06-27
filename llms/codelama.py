import requests
import subprocess  # Imported but not used

def query_codelama(user_input):
    """
    Always use the remote Cloudflare tunnel for CodeLlama.
    """
   response = requests.post(
    "https://toolbar-thorough-families-pcs.trycloudflare.com/api/generate",
    json={
        "model": "codellama",
        "prompt": user_input
    }
)

    response.raise_for_status()
    return response.json()["response"]
