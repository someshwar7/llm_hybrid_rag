import requests

def query_mistral(user_input):
    """
    Query Mistral through your Cloudflare tunnel.
    """
    response = requests.post(
        "https://remedies-telling-di-continent.trycloudflare.com/api/generate",
        json={
            "model": "mistral",
            "prompt": user_input,
            "stream": False  # Ollama expects this field
        }
    )
    response.raise_for_status()
    return response.json()
