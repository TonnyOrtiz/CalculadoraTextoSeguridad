from model.parser import Parser
from model.calculator import Calculator
from model.usersManager import UsersManager
from view.view import View
from model.session import Session
from utils.log import Log

class Controller:
    
    def __init__(self):
        self.usersManager = UsersManager()
        self.session = None
        self.log = Log()

    def login(self):
        idEntered = View.getUsername()
        password = View.getPassword()
        if not self.usersManager.validateUser(idEntered, password) :
            View.displayError(View.INVALID_AUTH)
            self.log.addEntry(idEntered , Log.F_LOGIN, False)
        else:
            self.session = Session(idEntered, self.usersManager.isAdmin(idEntered))
            self.log.addEntry(self.session.userId, Log.LOGIN, True)

    def calculate(self, expression):
        try:
            result = Parser.parseExpression(expression)
            result = Calculator.calculateExpression(result)
            View.displayResult(result)
            self.log.addEntry(self.session.userId, Log.CALCULATION, True)
        except Exception as e:
            View.displayError(View.INVALID_EXPRESSION)
            self.log.addEntry(self.session.userId, Log.F_CALCULATION, False)
            
    def createUser(self):
        isAdmin = View.getIsAdmin()
        idEntered = View.getNewUsername()
        try:
            if self.usersManager.createUser(idEntered, View.getNewPassword(), isAdmin):
                View.displaySuccess(View.USER_CREATED)
                self.log.addEntry(self.session.userId, Log.CREATE+". Nuevo Usuario: "+ idEntered, True)
        except Exception as e:
            View.displayError(View.USER_NOT_CREATED)
            self.log.addEntry(self.session.userId, Log.F_CREATE, False)

    def createFirstUser(self):
        idEntered = View.getNewUsername()
        try:
            if self.usersManager.createUser(idEntered, View.getNewPassword(), True):
                View.displaySuccess(View.USER_CREATED)
                self.log.addEntry("N/A", Log.CREATE+". Primer Usuario Administrador: "+ idEntered, True)
        except Exception as e:
            View.displayError(View.USER_NOT_CREATED)
            self.log.addEntry(self.session.userId, Log.F_CREATE, False)
        
    def run(self):
        if not self.usersManager.validateFile():
            View.displayWarning(View.USER_FILE_NOT_FOUND)
            self.log.addEntry("N/A", Log.USER_FILE, True)
            self.createFirstUser()
        try:
            self.login()   
            while self.session:
                if self.session.isAdministrator:
                    option = View.showMenuAdmin()
                    if option == "1":
                        self.calculate(View.getExpression())
                    elif option == "2":
                        self.createUser()
                    elif option == "0":
                        View.display("¡Adiós!")
                        self.log.addEntry(self.session.userId, Log.LOGOUT, True)
                        self.session = None
                    else:
                        View.displayError(View.INVALID_OPTION)
                        View.display("-----------------------------------")
                else:
                    option = View.showMenuUser()     
                    if option == "1":
                        self.calculate(View.getExpression())
                    elif option == "0":
                        View.display("¡Adiós!")
                        self.log.addEntry(self.session.userId, Log.LOGOUT, True)
                        self.session = None
                    else:
                        View.displayError(View.INVALID_OPTION)
                        View.display("-----------------------------------")
        except KeyboardInterrupt:
            View.displayWarning("\nInterrumpido por el usuario.")
            if self.session:
                self.log.addEntry(self.session.userId, Log.LOGOUT, True)
            else:
                self.log.addEntry("N/A", Log.KEYBOARD_INTERRUPT, True)
            sys.exit(0)
        except Exception as e:
            View.displayError(f"Error: {e}")
            self.log.addEntry(self.session.userId, Log.F_LOGOUT, False)
            sys.exit(1)
            