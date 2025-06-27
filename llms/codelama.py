import requests

def query_codelama(user_input):
    """
    Query CodeLlama through your Cloudflare tunnel.
    """
    response = requests.post(
        "https://remedies-telling-di-continent.trycloudflare.com/api/generate",
        json={
            "model": "codellama",
            "prompt": user_input,
            "stream": False  # required for Ollama's API if you want whole output at once
        }
    )
    response.raise_for_status()
    return response.json()
