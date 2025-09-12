"""Basic math operations collected in a class."""

class Operations:
    """
    A class to group simple math operations.
     Refactor note: In Module 2 we had free functions, 
       now they are wrapped inside a class as static methods 
       for better organization (OOP principle: encapsulation).
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """Return a + b (sum of two numbers)."""
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """Return a - b (difference between two numbers)."""
        return a-b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """Return a * b (product of two numbers)."""
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Return a / b (quotient of two numbers).

        👉 Refactor note: Added a defensive check before dividing.
           If b == 0, raise a ValueError with a clear message.
           This matches the tests and avoids runtime crash.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
