from model.parser import Parser
from model.calculator import Calculator
from utils.log import Log

class CalculatorController:
    def __init__(self, controller):
        self.controller = controller

    def calculate(self, expression):
            try:
                result = Parser.parseExpression(expression)
                result = Calculator.calculateExpression(result)
                Log.addEntry(self.controller.session().userId, Log.CALCULATION, True)
                return True, result
            except Exception as e:
                Log.addEntry(self.controller.session().userId, Log.F_CALCULATION, False)
                return False, str(e)