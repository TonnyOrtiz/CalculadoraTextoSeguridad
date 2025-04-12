class Parser:
    WORD_TO_NUMBER = {
        "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
        "once": 11, "doce": 12, "trece": 13, "catorce": 14,
        "quince": 15, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18,
        "diecinueve": 19, "veinte": 20
    }

    TENS_TO_NUMBER = {
        "treinta": 30, "cuarenta": 40, "cincuenta": 50,
        "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
    }
    TWENTY_WORD = "veinti"
    TWENTY_NUMBER = 20

    OPERATORS = ["+", "-", "*", "/"]
    PARENTHESES = ["(", ")"]


    @staticmethod
    def parseExpression(expression: str) -> list:
        try:
            
            return Parser.wordToNum(expression)
        except Exception as e:
            raise ValueError(f"Invalid expression: {expression}") from e
    
    def wordToNum(expression):
        # Preprocess the expression to add spaces around parentheses
        for p in Parser.PARENTHESES:
            expression = expression.replace(p, f" {p} ")

        # Add spaces around operators if not already spaced
        for op in Parser.OPERATORS:
            expression = expression.replace(op, f" {op} ")

        # Add spaces around "y" (and) for compound numbers
        expression = expression.replace("y", " y ")
        
        # Split the expression into words.
        words = expression.split()
        tokens = []  # List to store the parsed tokens
        i = 0

        while i < len(words):
            word = words[i]
            if word in Parser.WORD_TO_NUMBER:
                tokens.append(Parser.WORD_TO_NUMBER[word])
            elif word.startswith(Parser.TWENTY_WORD) and len(word) > 6:
                base = Parser.TWENTY_NUMBER
                suffix = word[6:]
                if suffix in Parser.WORD_TO_NUMBER:
                    tokens.append(base + Parser.WORD_TO_NUMBER[suffix])
            elif word in Parser.TENS_TO_NUMBER:
                # Check for compound numbers like "cuarenta y dos"
                if i + 2 < len(words) and words[i + 1] == "y" and words[i + 2] in Parser.WORD_TO_NUMBER:
                    tokens.append(Parser.TENS_TO_NUMBER[word] + Parser.WORD_TO_NUMBER[words[i + 2]])
                    i += 2  # Skip "y" and the unit word
                else:
                    tokens.append(Parser.TENS_TO_NUMBER[word])
            elif word in Parser.OPERATORS:
                tokens.append(word)
            elif word in Parser.PARENTHESES:
                tokens.append(word)
            else:
                raise ValueError(f"Unknown word in expression: {word}")
            i += 1

        return tokens  # Return the list of tokens