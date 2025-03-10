# Vision-Based Breakfast Inspection with Ollama

This project utilizes **Ollama** model to analyze breakfast images and check if the ingredients meet specific requirements. The model checks for the presence of ingredients such as eggs, toast, bacon, hashbrowns, and others, ensuring they meet criteria like proper cooking and quantity.

## Description

The application analyzes the given image of a breakfast and compares it against predefined criteria (e.g., whether there are two hashbrowns, whether the egg has a yellow yolk in the center, etc.).

## Getting Started

### 1. Clone the repository:
```
git clone https://github.com/username/my_vision_project.git
```

### 2. Navigate to the project directory:
```
cd my_vision_project
```

### 3. Create a virtual environment:
```
python -m venv .venv
```

### 4. Activate the virtual environment:
- For **Windows**:
```
.venv\Scripts\activate
```
- For **Linux/macOS**:
```
source .venv/bin/activate
```

### 5. Install project dependencies:
```
pip install -r requirements.txt
```

### 6. Set up environment variables:
Create a `.env` file in the root directory of the project and add the following configuration:

```ini
OLLAMA_PATH=C:\Users\YOUR_USER\AppData\Local\Programs\Ollama
OLLAMA_MODEL=llava:13b
OLLAMA_API_URL=http://localhost:11434/api/generate
```

- **OLLAMA_PATH**: Path where Ollama is installed.
- **OLLAMA_MODEL**: The model you want to use for analysis.
- **OLLAMA_API_URL**: The API endpoint for the Ollama server.

### 7. Run the application:
```
python main.py test.png "Describe the ingredients in this breakfast and check if they meet the following requirements:"
```

This will process the `test.png` image and check the breakfast ingredients against the provided requirements.

---

## Example Requirements

The following requirements are used to inspect the breakfast:

1. **Hashbrowns**: Two pieces, golden brown, evenly cooked, not burnt.
2. **Sausage**: One piece, fully cooked, golden-brown, crispy outside.
3. **Egg**: Yellow yolk in the center, not square-shaped, yolk not broken, egg white set and fully cooked.
4. **Toast**: Two slices of bread, cut diagonally, no burnt edges.
5. **Bacon**: Fully cooked, crisp but not burnt.
6. **Beans**: Approximately 85g of beans, in a small portion.

The program will return a list in the format `[Yes/No, Yes/No, Yes/No, Yes/No, Yes/No, Yes/No]` with explanations when any "No" answers are given.

---

## Logs

Logs of the application's execution are stored in the `logs/app.log` file. You can check this file for detailed error messages and other information.

---

## Important Notes

- For proper functioning, the **Ollama model** must be installed locally. You can download and install it from [Ollama's official website](https://ollama.com/download).
- Ensure your system meets the necessary resource requirements to run the Ollama model locally.
- This project does not require internet access once Ollama is installed, as it runs entirely locally.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Troubleshooting

- **"Ollama not installed" error**: This usually occurs when Ollama is not installed or the path is not set correctly in the `.env` file. Please ensure that Ollama is installed and its path is correctly configured.
- **Model not found**: If the specified model (`llava:13b`) is not found, try running `ollama pull llava:13b` from your terminal.

---

## Contributing

Feel free to fork this repository, submit pull requests, and contribute to the project. If you encounter any issues, please open an issue on GitHub.

---

## Acknowledgments

- This project uses the **Ollama** API to perform image-based analysis. 
- Special thanks to the **Ollama team** for providing this powerful multimodal model.