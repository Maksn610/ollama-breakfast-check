from .api_client import generate_response
from .image_processor import validate_image
from .prompt_builder import build_prompt

def analyze_image(image_path: str, question: str) -> dict:
    validate_image(image_path)
    prompt = build_prompt(question)
    return generate_response(prompt, image_path)
