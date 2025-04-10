class Parser:

    def parse_expression(self, expression: str) -> list:
        try:
            word_to_number = {
                "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
                "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
                "once": 11, "doce": 12, "trece": 13, "catorce": 14,
                "quince": 15, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18,
                "diecinueve": 19, "veinte": 20
            }

            tens_to_number = {
                "treinta": 30, "cuarenta": 40, "cincuenta": 50,
                "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
            }

            operators = ["+", "-", "*", "/"]
            parentheses = ["(", ")"]

            def word_to_num(expression):
                # Preprocess the expression to add spaces around parentheses
                for p in parentheses:
                    expression = expression.replace(p, f" {p} ")

                words = expression.split()
                tokens = []  # List to store the parsed tokens
                i = 0

                while i < len(words):
                    word = words[i]
                    if word in word_to_number:
                        tokens.append(word_to_number[word])
                    elif word.startswith("veinti") and len(word) > 6:
                        base = 20  # Hardcoded base value for "veinti"
                        suffix = word[6:]
                        if suffix in word_to_number:
                            tokens.append(base + word_to_number[suffix])
                    elif word in tens_to_number:
                        # Check for compound numbers like "cuarenta y dos"
                        if i + 2 < len(words) and words[i + 1] == "y" and words[i + 2] in word_to_number:
                            tokens.append(tens_to_number[word] + word_to_number[words[i + 2]])
                            i += 2  # Skip "y" and the unit word
                        else:
                            tokens.append(tens_to_number[word])
                    elif word in operators:
                        tokens.append(word)
                    elif word in parentheses:
                        tokens.append(word)
                    else:
                        raise ValueError(f"Unknown word in expression: {word}")
                    i += 1

                return tokens  # Return the list of tokens

            return word_to_num(expression)
        except Exception as e:
            raise ValueError(f"Invalid expression: {expression}") from e
