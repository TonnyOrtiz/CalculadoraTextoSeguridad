from models.parser import Parser

parser = Parser()
parsed_expression = parser.parse_expression("veintidos * (veintitres + cuatro)") 
print(parsed_expression)