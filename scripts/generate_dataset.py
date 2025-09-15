import sympy
import random
from tqdm import tqdm
import os

# --- Parameters ---
NUM_EXAMPLES = 10000  # Isko 20000000 (2 crore) ya zyada karein final run ke liye
FILE_PATH = "../data/math_dataset.txt"

# --- Helper Functions ---

def generate_linear_equation():
    """Ek random linear equation banata aur solve karta hai."""
    x = sympy.symbols('x')
    a = random.randint(-50, 50)
    while a == 0:
        a = random.randint(-50, 50)
    b = random.randint(-50, 50)
    c = random.randint(-50, 50)
    equation = sympy.Eq(a*x + b, c)
    try:
        solution = sympy.solve(equation, x)
        if solution:
            problem_str = f"{a}*x + {b} = {c}"
            solution_str = f"x = {solution[0]}"
            return f"Problem: {problem_str} | Solution: {solution_str};"
    except Exception:
        return None

def generate_quadratic_equation():
    """Ek random quadratic equation banata aur solve karta hai."""
    x = sympy.symbols('x')
    a = random.randint(-20, 20)
    while a == 0:
        a = random.randint(-20, 20)
    b = random.randint(-20, 20)
    c = random.randint(-20, 20)
    equation = sympy.Eq(a*x**2 + b*x + c, 0)
    try:
        solutions = sympy.solve(equation, x)
        if solutions:
            problem_str = f"{a}*x**2 + {b}*x + {c} = 0"
            solution_str = f"x = {solutions}"
            return f"Problem: {problem_str} | Solution: {solution_str};"
    except Exception:
        return None

# --- Main Execution ---

if __name__ == "__main__":
    problem_generators = [
        generate_linear_equation, 
        generate_quadratic_equation
    ]
    print(f"Generating {NUM_EXAMPLES} examples for your dataset...")
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        for _ in tqdm(range(NUM_EXAMPLES)):
            generator_func = random.choice(problem_generators)
            line = generator_func()
            if line:
                f.write(line + "\n")
    print(f"\nDataset generation complete! File saved at: {FILE_PATH}")
    file_size_mb = os.path.getsize(FILE_PATH) / (1024 * 1024)
    print(f"Final file size: {file_size_mb:.2f} MB")