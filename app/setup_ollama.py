import platform
import subprocess
import sys
import logging
from app.config import OLLAMA_MODEL
from app.path_manager import add_ollama_to_path

logger = logging.getLogger(__name__)

def check_ollama_installed():
    try:
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True, check=True)
        logger.info(f"Ollama found: {result.stdout.strip()}")
        return True
    except:
        logger.warning("Ollama not found in PATH.")
        return False

def install_ollama():
    if platform.system() == "Windows":
        add_ollama_to_path()
        logger.info("Please install Ollama manually from https://ollama.com/download for Windows.")
        sys.exit(1)
    elif platform.system() == "Linux":
        subprocess.run(["curl -fsSL https://ollama.com/install.sh | sh"], shell=True, check=True)

def check_model_installed(model: str):
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
    return model in result.stdout

def pull_model(model: str):
    subprocess.run(["ollama", "pull", model], check=True)

def setup_ollama_and_model():
    if not check_ollama_installed():
        install_ollama()
    if not check_model_installed(OLLAMA_MODEL):
        pull_model(OLLAMA_MODEL)
