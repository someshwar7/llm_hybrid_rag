import requests
import subprocess  # Imported but not used

def query_mistral(user_input):
    """
    Always use the remote Cloudflare tunnel for Mistral.
    """
    response = requests.post(
    "https://toolbar-thorough-families-pcs.trycloudflare.com/api/generate",
    json={
        "model": "mistral",
        "prompt": user_input
    }
)

    response.raise_for_status()
    return response.json()["response"]
