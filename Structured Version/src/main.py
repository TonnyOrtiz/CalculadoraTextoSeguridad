from models.parser import Parser

parser = Parser()
parsed_expression = parser.parseExpression("veintidos * (veintitres + cuatro)") 
print(parsed_expression)