"""Simple REPL calculator that uses the Operations class."""

from app.operations import Operations


def calculator() -> None:
    """
    A Read-Eval-Print Loop (REPL) calculator.

    Refactor note: 
       - Instead of importing individual functions, 
         we now import the Operations class.
       - We call static methods through the class, 
         which is cleaner and shows OOP usage.
    """
    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:
        # Ask the user for input
        user_input = input(
            "Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: "
        )

        # Exit condition (handles exit, EXIT, Exit, etc.)
        if user_input.lower().strip() == "exit":
            print("Exiting calculator...")
            break

        try:
            # Split the input into three parts: operation and two numbers
            operation, num1, num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            # If input format is wrong
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue

        # Normalize operation to lowercase
        operation = operation.lower()

        # Match operation and call the correct static method
        if operation == "add":
            result = Operations.addition(num1, num2)
        elif operation == "subtract":
            result = Operations.subtraction(num1, num2)
        elif operation == "multiply":
            result = Operations.multiplication(num1, num2)
        elif operation == "divide":
            try:
                result = Operations.division(num1, num2)
            except ValueError as e:
                # Handle division by zero gracefully
                print(e)
                continue
        else:
            # Handle unsupported operation
            print(
                f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide."
            )
            continue

        # Show result
        print(f"Result: {result}")