from app.service import analyze_image
from app.setup_ollama import setup_ollama_and_model
from app.logger_setup import setup_logging
import sys

def main():
    setup_logging()
    setup_ollama_and_model()

    if len(sys.argv) != 3:
        print("Usage: python main.py <image_path> <question>")
        sys.exit(1)

    image_path, question = sys.argv[1], sys.argv[2]
    result = analyze_image(image_path, question)
    print("Response:", result['response'])

if __name__ == "__main__":
    main()
