import sys
from model.parser import Parser
from model.calculator import Calculator
from view.view import View
from controller.usersManager import UsersManager
from controller.session import Session

class Controller:
    
    def __init__(self):
        self.view = View()
        self.parser = Parser()
        self.calculator = Calculator()
        self.usersManager = UsersManager()
        self.args = sys.argv[1:]
        self.argc = len(self.args)
        self.session = None

    def login(self):
        idEntered = self.view.getUsername()
        passwordHashed = self.view.getPassword()
        if not self.usersManager.validateUser(idEntered, passwordHashed) :
            self.view.displayError(self.view.INVALID_AUTH)
        else:
            self.session = Session(idEntered, self.usersManager.isAdmin(idEntered))

    def calculate(self, expression):
        try:
            result = self.parser.parseExpression(expression)
            result = self.calculator.calculateExpression(result)
            self.view.printResult(result)
        except Exception as e:
            self.view.displayError(self.view.INVALID_EXPRESSION)
            
    def createUser(self):
        idEntered = self.view.getNewUsername()
        passwordEntered = self.view.getNewPassword()
        isAdmin = self.view.getInput("¿Es administrador? (s/n): ").lower() == "s"
        try:
            if self.usersManager.createUser(idEntered, passwordEntered, isAdmin):
                self.view.display("Usuario creado exitosamente.")
        except Exception as e:
            self.view.displayError(self.view.USER_NOT_CREATED)

    def run(self):
        self.login()   
        while self.session:
            if self.session.isAdministrator:
                option = self.view.showMenuAdmin()
                if option == "1":
                    self.calculate(self.view.getExpression)
                if option == "2":
                    self.createUser()
                if option == "0":
                    self.view.display("¡Adiós!")
                    self.session = None
            else:
                option = self.view.showMenuUser()     
                if option == "1":
                    self.calculate(self.view.getExpression)
                if option == "0":
                    self.view.display("¡Adiós!")
                    self.session = None
            