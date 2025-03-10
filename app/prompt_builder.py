def build_prompt(question: str) -> str:
    detailed_requirements = """
You are a food inspection AI. Analyze the image and identify the following breakfast ingredients. For each item, please answer the following:

1. List each ingredient visible in the image.
2. Count the number of pieces of each ingredient present.
3. For each ingredient, check if it meets the following requirements:
   - Hashbrowns: Two pieces, golden brown, evenly cooked, not burnt.
   - Sausage: One piece only, fully cooked, golden-brown, crispy outside.
   - Egg: Yellow yolk in the center, not square-shaped, yolk not broken, fully cooked egg white.
   - Toast: Two slices of bread, cut diagonally, no burnt edges.
   - Bacon: Fully cooked, crisp but not burnt.
   - Beans: Approximately 85g, in a small portion.

If any ingredient does not meet the requirements, provide a detailed explanation of why it does not match.

Provide the response in the following format:
1. Ingredient name: [Yes/No], [Number of pieces], [Explanation if "No"]
2. Ingredient name: [Yes/No], [Number of pieces], [Explanation if "No"]
...
"""
    return f"<image>\n{question}\n\n{detailed_requirements}"
