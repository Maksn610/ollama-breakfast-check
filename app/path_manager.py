import winreg
import logging
from app.config import OLLAMA_PATH

logger = logging.getLogger(__name__)

def add_ollama_to_path():
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Environment",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE
        ) as key:
            current_path, _ = winreg.QueryValueEx(key, "Path")
            paths = current_path.split(";")
            if OLLAMA_PATH not in paths:
                paths.append(OLLAMA_PATH)
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, ";".join(paths))
                logger.info(f"Added Ollama path '{OLLAMA_PATH}' to PATH. Restart terminal to apply.")
            else:
                logger.info("Ollama path already exists in PATH.")
    except Exception as e:
        logger.error(f"Failed to update PATH: {e}")
