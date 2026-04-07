
import requests

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": prompt,
                "stream": False
            },
            timeout=20
        )

        data = response.json()
        return data.get("response", "")

    except Exception as e:
        return f"Ollama error: {str(e)}"
