from model.usersManager import UsersManager
from model.session import Session
from utils.log import Log

class UsersController :
    def __init__(self, controller):
        self.controller = controller
        self.session = None

    def createNewUser(self,idEntered, password, isAdmin):
        try:
            if UsersManager.createUser(idEntered, password, isAdmin):
                Log.addEntry(self.session.userId, Log.CREATE+". Nuevo Usuario: "+ idEntered, True)
                return True
        except Exception as e:
            Log.addEntry(self.session.userId, Log.F_CREATE, False)
            return False

    def createFirstUser(self, idEntered, password):
        try:
            if UsersManager.createUser(idEntered, password, True):
                Log.addEntry("N/A", Log.CREATE+". Primer Usuario Administrador: "+ idEntered, True)
                return True
        except Exception as e:
            Log.addEntry(self.session.userId, Log.F_CREATE, False)
            return False

    def login(self, idEntered, password):
        loginSuccessful = UsersManager.validateUser(idEntered, password)
        if loginSuccessful:
            self.session = Session(idEntered, UsersManager.isAdmin(idEntered))
        Log.addEntry(idEntered ,Log.LOGIN if loginSuccessful else Log.F_LOGIN, loginSuccessful)
        return loginSuccessful, idEntered
    
    def logout(self):
        if self.session:
            Log.addEntry(self.session.userId, Log.LOGOUT, True)
            self.session = None
            return True
        else:
            Log.addEntry("N/A", Log.F_LOGOUT, False)
            return False
    
    def forcedLogout(self, userInitiated = False):
        if userInitiated:
            if self.session:
                Log.addEntry(self.session.userId, Log.KEYBOARD_INTERRUPT, True)
            else:
                Log.addEntry("N/A", Log.KEYBOARD_INTERRUPT, True)
        else:
            if self.session:
                Log.addEntry(self.session.userId, Log.F_LOGOUT, False)
            else:
                Log.addEntry("N/A", Log.F_LOGOUT, False)
            
    
    def initialized(self):
        if not UsersManager.validateFile():
            Log.addEntry("N/A", Log.USER_FILE, True)
            return False
        return True
            