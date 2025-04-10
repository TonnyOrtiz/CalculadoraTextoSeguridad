class Calculator:
    def calculateExpression(self, expression: str) -> float:
        try:
            result = 0; # Placeholder for actual calculation logic
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {expression}") from e
    
    def add(self, a: float, b: float) -> float:
        return a + b
    def subtract(self, a: float, b: float) -> float:
        return a - b
    def multiply(self, a: float, b: float) -> float:
        return a * b
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b