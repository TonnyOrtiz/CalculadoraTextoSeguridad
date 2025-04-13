from view.view import View

class ViewController :
    # Constants
    ADMIN_OPTIONS = { "1", "2", "0" }
    USER_OPTIONS = { "1", "0" }
    CALCULATION = "1"
    CREATE_USER = "2"
    EXIT = "0"

    def __init__(self, controller):
        self.controller = controller

    def inputLogin(self):
        idEntered = View.getUsername()
        password = View.getPassword()
        return idEntered, password
        
    def loginResult(self, successful, idEntered):
        if not successful:
            View.displayError(View.INVALID_AUTH)

    def inputFirstUser(self):
        View.displayWarning(View.USER_FILE_NOT_FOUND)
        View.display(View.FIRST_USER)
        return View.getNewUsername(), View.getNewPassword()
    
    def inputNewUser(self):
        isAdmin = View.getIsAdmin()
        idEntered = View.getNewUsername()
        password = View.getNewPassword()
        return idEntered, password, isAdmin
    
    def userCreationResult(self, successful):
        if successful:
            View.displaySuccess(View.USER_CREATED)
        else:
            View.displayError(View.USER_NOT_CREATED)

    def inputExpression(self):
        return View.getExpression()
    
    def expressionResult(self, successful, result):
        if successful:
            View.displayResult(result)
        else:
            View.displayError(View.INVALID_EXPRESSION)

    def Menu(self):
        if self.controller.session().isAdministrator:
            return self.menuAdmin()
        else:
            return self.menuUser()

    def menuAdmin(self):
        option = None
        while not option:
            option = View.showMenuAdmin().strip()
            if option not in self.ADMIN_OPTIONS:
                View.displayError(View.INVALID_OPTION)
                View.display("-----------------------------------")
                option = None
        return option

    def menuUser(self):
        option = None
        while not option:
            option = View.showMenuUser().strip()
            if option not in self.USER_OPTIONS:
                View.displayError(View.INVALID_OPTION)
                View.display("-----------------------------------")
                option = None
        return option

    def goodbye(self):
        View.display("¡Adiós!")

    def keyboardInterrupt(self):
        View.displayWarning("\nInterrumpido por el usuario.")

    def exception(self, e):
        View.displayError(f"Error: {e}")