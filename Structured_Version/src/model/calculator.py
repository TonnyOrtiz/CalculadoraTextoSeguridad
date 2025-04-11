class Calculator:
    def calculateExpression(self, tokens: list) -> float:
        try:
            
            result = Calculator.evaluateTokens(self, tokens)
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {tokens}") from e
    
    def evaluateTokens(self, tokens: list) -> float:
        # Handle parentheses first
        i = 0
        while i < len(tokens):
            if isinstance(tokens[i], str) and tokens[i] == "(":
                # Find the matching closing parenthesis
                open_index = i
                close_index = i + 1
                depth = 1
                while close_index < len(tokens) and depth > 0:
                    if tokens[close_index] == "(":
                        depth += 1
                    elif tokens[close_index] == ")":
                        depth -= 1
                    close_index += 1

                if depth != 0:
                    raise ValueError("Mismatched parentheses")

                # Evaluate the expression inside the parentheses
                inner_result = self.evaluateTokens(tokens[open_index + 1 : close_index - 1])

                # Replace the parentheses and their contents with the result
                tokens = tokens[:open_index] + [inner_result] + tokens[close_index:]
                i = open_index  # Reset index to the position of the result
            else:
                i += 1

        # Handle multiplication and division first
        i = 0
        while i < len(tokens):
            if isinstance(tokens[i], str) and tokens[i] in ("*", "/"):
                if tokens[i] == "*":
                    result = self.multiply(tokens[i - 1], tokens[i + 1])
                elif tokens[i] == "/":
                    result = self.divide(tokens[i - 1], tokens[i + 1])

                # Replace the operator and its operands with the result
                tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
                i -= 1  # Adjust index after modifying the list
            else:
                i += 1

        # Handle addition and subtraction
        i = 0
        while i < len(tokens):
            if isinstance(tokens[i], str) and tokens[i] in ("+", "-"):
                if tokens[i] == "+":
                    result = self.add(tokens[i - 1], tokens[i + 1])
                elif tokens[i] == "-":
                    result = self.subtract(tokens[i - 1], tokens[i + 1])

                # Replace the operator and its operands with the result
                tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
                i -= 1  # Adjust index after modifying the list
            else:
                i += 1

        # The final result will be the only element left in the tokens list
        return tokens[0]
        
        
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
