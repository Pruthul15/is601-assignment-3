# Assignment 3: Command-Line Calculator with REPL

A robust command-line calculator built in Python with continuous integration and 100% test coverage.

## What This Does

This is a simple calculator that runs in your terminal. You can do basic math operations and it keeps running until you tell it to stop. It has proper error handling and comprehensive testing.

## Features

- REPL (Read-Eval-Print Loop) interface for continuous use
- Basic arithmetic operations: add, subtract, multiply, divide
- Input validation and error handling
- Division by zero protection
- 100% test coverage with automated testing
- GitHub Actions for continuous integration

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Pruthul15/is601-assignment-3.git
cd is601-assignment-3
```

### 2. Create Virtual Environment
```bash
# Linux/macOS/WSL
python3 -m venv venv
source venv/bin/activate

# Windows PowerShell
python -m venv venv
venv\Scripts\Activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## How to Use

### Run the Calculator
```bash
python main.py
```

### Example Session
```
Welcome to the calculator REPL! Type 'exit' to quit.

Enter an operation (add, subtract, multiply, divide) and two numbers:
> add 3 5
Result: 8.0

> multiply 4 7
Result: 28.0

> divide 10 0
Division by zero is not allowed.

> subtract 15 8
Result: 7.0

> exit
Goodbye!
```

### Available Operations
- `add` - Addition
- `subtract` - Subtraction  
- `multiply` - Multiplication
- `divide` - Division (with zero protection)
- `exit` - Quit the calculator

## Project Structure

```
is601-assignment-3/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions workflow
├── app/
│   ├── __init__.py
│   ├── calculator/
│   │   └── __init__.py        # Main calculator logic
│   └── operations/
│       ├── __init__.py        # Operation functions
│       └── division/
│           └── __init__.py    # Division with error handling
├── tests/
│   ├── test_calculator.py     # Unit tests
│   └── test_operations.py     # Parameterized tests
├── main.py                    # Entry point
├── pytest.ini                # Test configuration
├── requirements.txt           # Dependencies
├── LICENSE
└── README.md
```

## Testing

### Run All Tests
```bash
pytest
```

### Run Tests with Coverage Report
```bash
pytest --cov=app --cov-report=term-missing
```

### Test Coverage
This project maintains **100% test coverage** as enforced by:
- Local pytest configuration
- GitHub Actions CI pipeline
- Comprehensive unit and parameterized tests

## Best Practices Applied

- **DRY Principle**: No repeated code, modular design
- **Input Validation**: Handles invalid inputs gracefully
- **Error Handling**: Comprehensive error management
- **Testing**: 100% coverage with unit and parameterized tests
- **Documentation**: Clear code comments and this README
- **CI/CD**: Automated testing with GitHub Actions

## GitHub Actions

The project uses GitHub Actions to automatically:
- Run all tests on every push
- Check for 100% test coverage
- Fail the build if coverage drops below 100%
- Ensure code quality and reliability

## Development

If you want to modify the calculator:

1. Make your changes to the code
2. Add corresponding tests
3. Run `pytest` to ensure 100% coverage
4. Commit and push - GitHub Actions will validate everything

## Requirements

- Python 3.x
- pytest (for testing)
- pytest-cov (for coverage reporting)

## Error Handling

The calculator handles these error cases:
- Division by zero
- Invalid operation names
- Non-numeric inputs
- Empty inputs
- Invalid number of arguments

All errors display helpful messages and allow you to try again.