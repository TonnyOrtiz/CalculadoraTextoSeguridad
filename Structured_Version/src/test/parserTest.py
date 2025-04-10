from model.parser import Parser

def main():
    parser = Parser()
    parsed_expression = parser.parseExpression("veintidos * (veintitres + cuatro)") 
    print(parsed_expression)

if __name__ == "__main__":
    main()