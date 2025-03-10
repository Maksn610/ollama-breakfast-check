import os
import base64

def validate_image(image_path: str):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Зображення за шляхом {image_path} не знайдено.")

def load_image_base64(image_path: str) -> str:
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode('utf-8')
