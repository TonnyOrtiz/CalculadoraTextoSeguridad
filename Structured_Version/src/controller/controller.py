import sys
from model.parser import Parser
from model.calculator import Calculator
from view.view import View

class Controller:
    def __init__(self):
        self.view = View()
        self.parser = Parser()
        self.calculator = Calculator()
        self.args = sys.argv[1:]
        self.argc = len(self.args)

    def run(self):
        while True:
            option = self.view.showMenuUser()
            if option == "1":
                expression = self.view.getInput("Ingrese la expresión: ")
                try:
                    result = self.parser.parseExpression(expression)
                    result = self.calculator.calculateExpression(result)
                    self.view.display(f"Resultado: {result}")
                except Exception as e:
                    self.view.display(f"Error al procesar la expresión: {e}")
            if option == "2":
                self.view.display("¡Adiós!")
                break