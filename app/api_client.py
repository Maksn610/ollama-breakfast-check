import requests
import base64
from app.config import OLLAMA_API_URL, OLLAMA_MODEL

def generate_response(prompt: str, image_path: str) -> dict:
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "images": [img_base64],
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    return response.json()
