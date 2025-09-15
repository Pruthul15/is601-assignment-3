#  Module 3 – Command-Line Calculator

## 🎯 Objective
For this assignment, we extended the calculator project to build a robust **command-line calculator** in Python using best practices:

- **REPL (Read–Eval–Print Loop)** interface for continuous interaction  
- Arithmetic operations: **add, subtract, multiply, divide**  
- Input validation and error handling (e.g., divide by zero)  
- Clean project structure following the **DRY principle**  
- **100% unit test coverage** enforced with `pytest`  
- Continuous Integration (CI) with **GitHub Actions** to run tests automatically  


## 📂 Project Structure


assignment3/
├─ .github/
│ └─ workflows/
│ └─ tests.yml # GitHub Actions workflow
├─ app/
│ ├─ init.py
│ ├─ main.py # REPL entry point
│ ├─ calculator/
│ │ └─ init.py
│ └─ operations/
│ ├─ init.py
│ └─ division/
│ └─ init.py
├─ tests/
│ ├─ test_calculator.py # unit tests
│ └─ test_operations.py # parameterized tests
├─ pytest.ini # enforces 100% coverage
├─ requirements.txt
├─ LICENSE
└─ README.md

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:Pruthul15/is601-assignment-3.git
cd assignment3



2. Create and Activate Virtual Environment

Linux/macOS (WSL included):
python3 -m venv venv
source venv/bin/activate

Windows (PowerShell):
python -m venv venv
venv\Scripts\Activate


3. Install Dependencies
pip install -r requirements.txt

▶️ Run the Calculator (REPL)
python main.py


xample session:

Welcome to the calculator REPL! Type 'exit' to quit.

Enter an operation (add, subtract, multiply, divide) and two numbers:
> add 3 5
Result: 8.0

> divide 10 0
Division by zero is not allowed.

> exit 

Running Tests & Coverage

Run all tests:

pytest