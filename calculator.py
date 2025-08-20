class Calculator:
    """Simple calculator for basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        """Return a / b. Raise ValueError if b is 0."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
