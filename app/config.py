import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_PATH = os.getenv("OLLAMA_PATH", r"C:\Users\Default\AppData\Local\Programs\Ollama")
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llava")
