import sys
from model.parser import Parser
from model.calculator import Calculator
from model.usersManager import UsersManager
from view.view import View
from controller.session import Session
from utils.log import Log

class Controller:
    
    def __init__(self):
        self.view = View()
        self.parser = Parser()
        self.calculator = Calculator()
        self.usersManager = UsersManager()
        self.args = sys.argv[1:]
        self.argc = len(self.args)
        self.session = None
        self.log = Log()

    def login(self):
        idEntered = self.view.getUsername()
        passwordHashed = self.view.getPassword()
        if not self.usersManager.validateUser(idEntered, passwordHashed) :
            self.view.displayError(View.INVALID_AUTH)
            self.log.addEntry("N/A" , Log.F_LOGIN, False)
        else:
            self.session = Session(idEntered, self.usersManager.isAdmin(idEntered))
            self.log.addEntry(self.session.userId, Log.LOGIN, True)

    def calculate(self, expression):
        try:
            result = self.parser.parseExpression(expression)
            result = self.calculator.calculateExpression(result)
            self.view.displayResult(result)
            self.log.addEntry(self.session.userId, Log.CALCULATION, True)
        except Exception as e:
            self.view.displayError(View.INVALID_EXPRESSION)
            self.log.addEntry(self.session.userId, Log.F_CALCULATION, False)
            
    def createUser(self):
        idEntered = self.view.getNewUsername()
        passwordEntered = self.view.getNewPassword()
        isAdmin = self.view.getInput("¿Es administrador? (s/n): ").lower() == "s"
        try:
            if self.usersManager.createUser(idEntered, passwordEntered, isAdmin):
                self.view.displaySuccess(View.USER_CREATED)
                self.log.addEntry(self.session.userId, Log.CREATE+". Nuevo Usuario: "+ idEntered, True)
        except Exception as e:
            self.view.displayError(View.USER_NOT_CREATED)
            self.log.addEntry(self.session.userId, Log.F_CREATE, False)

    def run(self):
        try:
            self.login()   
            while self.session:
                if self.session.isAdministrator:
                    option = self.view.showMenuAdmin()
                    if option == "1":
                        self.calculate(self.view.getExpression())
                    if option == "2":
                        self.createUser()
                    if option == "0":
                        self.view.display("¡Adiós!")
                        self.log.addEntry(self.session.userId, Log.LOGOUT, True)
                        self.session = None
                else:
                    option = self.view.showMenuUser()     
                    if option == "1":
                        self.calculate(self.view.getExpression)
                    if option == "0":
                        self.view.display("¡Adiós!")
                        self.log.addEntry(self.session.userId, Log.LOGOUT, True)
                        self.session = None
        except KeyboardInterrupt:
            self.view.display("\nInterrumpido por el usuario.")
            self.log.addEntry(self.session.userId, Log.F_LOGOUT, False)
            sys.exit(0)
            