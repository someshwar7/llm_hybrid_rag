import requests

def query_mistral(user_input):
    """
    Always use the remote Cloudflare tunnel for Mistral.
    """
    response = requests.post(
        "https://remedies-telling-di-continent.trycloudflare.com/api/generate",
        json={
            "model": "mistral",
            "prompt": user_input
        }
    )
    response.raise_for_status()
    return response.json()["response"]
