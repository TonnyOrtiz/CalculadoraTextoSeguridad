import sys
from model.parser import Parser
from view.view import View

class Controller:
    def __init__(self):
        self.view = View()
        self.parser = Parser()
        self.args = sys.argv[1:]
        self.argc = len(self.args)

    def run(self):
        while True:
            option = self.view.showMenuUser()
            if option == "2":
                self.view.display("¡Adiós!")
                break