import sys
from controller.usersController import UsersController
from controller.viewController import ViewController
from controller.calculatorController import CalculatorController
from model.session import Session

class Controller:
    
    def __init__(self):
        self.viewController = ViewController(self)
        self.usersController = UsersController(self)
        self.calculatorController = CalculatorController(self)

    def session(self):
        return self.usersController.session

    def start(self):  
        if not self.usersController.initialized():
            self.viewController.userCreationResult(
                self.usersController.createFirstUser(*self.viewController.inputFirstUser())
            )       
        # login
        self.viewController.loginResult(
            *self.usersController.login(*self.viewController.inputLogin())
            )    
            
    def mainLoop(self):
        while self.session():
            option = self.viewController.Menu()
            if option == ViewController.CALCULATION:
                self.viewController.expressionResult(
                *self.calculatorController.calculate(self.viewController.inputExpression())
                )
            elif option == ViewController.CREATE_USER:
                self.viewController.userCreationResult(
                    self.usersController.createNewUser(*self.viewController.inputNewUser())
                )
            else:
                self.usersController.logout()
                self.viewController.goodbye()
    
    def run(self):
        try:
            # Initialize the users manager and check if the user file exists
            self.start()
            # Main loop
            self.mainLoop()
        except KeyboardInterrupt:
            # Handle keyboard interrupt gracefully
            self.usersController.forcedLogout(True)
            self.viewController.keyboardInterrupt()
            sys.exit(0)
        except Exception as e:
            # Handle other exceptions
            self.usersController.forcedLogout()
            self.viewController.exception(e)
            sys.exit(1)