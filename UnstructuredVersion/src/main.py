import getpass, sys
from datetime import datetime, timezone

# Constants ---------------------------------------------------
# File paths
usersArchive = "src/data/users.dat"
historyArchive = "src/data/history.log"

# Error messages   
INVALID_INPUT = "Entrada inválida."
USER_NOT_FOUND = "Usuario no encontrado."
EMPTY_USERNAME = "El ID de usuario no puede estar vacío."
EMPTY_PASSWORD = "La contraseña no puede estar vacía."
INVALID_AUTH = "Usuario o Contraseña inválidos."
USER_ALREADY_EXISTS = "El usuario ya existe."
PASSWORD_MISMATCH = "Las contraseñas no coinciden."
USER_NOT_CREATED = "El usuario no fue creado."
INVALID_EXPRESSION = "La expresión es inválida."
INVALID_MENU_OPTION = "La opción del menú es inválida."
USER_FILE_NOT_FOUND = "El archivo de usuarios no existe, \nesta puede ser la primera vez que se ejecuta el programa. \nSe creará un nuevo archivo de usuario."

# Success messages
USER_CREATED = "Usuario creado exitosamente."

# Log Entry Types:
LOGIN = "Inicio de sesión de usuario completado correctamente"
F_LOGIN = "Inicio de sesión de usuario fallido"
CREATE = "Creación de usuario completada correctamente"
F_CREATE = "Creación de usuario fallida"
CALCULATION = "Cálculo completado correctamente"
F_CALCULATION = "Cálculo fallido. Se produjo una excepción."
LOGOUT = "Usuario terminó sesión correctamente"
F_LOGOUT = "Se interrumpió la sesión del usuario"
KEYBOARD_INTERRUPT = "El usuario interrumpió la ejecución del programa"
USER_FILE = "Archivo de usuario creado correctamente"

# Log types:
SUCCESS = "CORRECTO"
ERROR = "FALLO"

def main():
    if not validateFile():
        displayWarning(USER_FILE_NOT_FOUND)
        logAddEntry("N/A", USER_FILE, True)
        createFirstUser()
    try:
        idEntered = getUsername()
        password = getPassword()
        if not validateUser(idEntered, password) :
            displayError(INVALID_AUTH)
            logAddEntry("N/A" , F_LOGIN, False)
        else:
            sessionId = idEntered
            sessionIsAdmin=isAdmin(idEntered)
            logAddEntry(sessionId, LOGIN, True)
            while sessionId:
                if sessionIsAdmin:
                    option = showMenuAdmin()
                    if option == "1":
                        calculate(getExpression())
                    if option == "2":
                        createUser()
                    if option == "0":
                        display("¡Adiós!")
                        logAddEntry(sessionId, LOGOUT, True)
                        sessionId = None
                else:
                    option = showMenuUser()     
                    if option == "1":
                        calculate(getExpression())
                    if option == "0":
                        display("¡Adiós!")
                        logAddEntry(self.session.userId, Log.LOGOUT, True)
                        self.session = None
    except KeyboardInterrupt:
        View.displayWarning("\nInterrumpido por el usuario.")
        logAddEntry(self.session.userId, Log.KEYBOARD_INTERRUPT, True)
        sys.exit(0)
    except Exception as e:
        View.displayError(f"Error: {e}")
        logAddEntry(self.session.userId, Log.F_LOGOUT, False)
        sys.exit(1)

if __name__ == "__main__":
    main()

def display(message):
    print(message)

def getInput(prompt):
    return input(prompt)

def showMenuAdmin():
    print("Menu de la Calculadora Peculiar")
    print("-----------------------------------")
    print("Por favor, seleccione una opción del menú:")
    print("1. Calcular expresión matemática con números en letras")
    print("2. Crear nuevo usuario")
    print("0. Salir")
    print("")
    return getInput("Ingrese su opción: ")

def showMenuUser():
    print("Menu de la Calculadora Peculiar")
    print("-----------------------------------")
    print("Por favor, seleccione una opción del menú:")
    print("1.Calcular expresión matemática con números en letras")
    print("0. Salir")
    print("")
    return getInput("Ingrese el número de opción: ")

def getUsername():
    idEntered = None
    while not idEntered:
        idEntered = input("Ingrese su ID de usuario: ")
        if idEntered:
            return idEntered
        displayError(EMPTY_USERNAME)
            
def getPassword():
    return getpass.getpass("Ingrese su contraseña: ")

def getNewPassword():
    temp =getpass.getpass("Ingrese la nueva contraseña: ")
    if temp == getpass.getpass("Confirme la nueva contraseña: "):
        return temp
    displayError(PASSWORD_MISMATCH)
    
def getNewUsername():
    idEntered = None
    while not idEntered:
        idEntered = input("Ingrese el nuevo ID de usuario: ")
        if idEntered:
            return idEntered
        view.displayError(view.EMPTY_USERNAME)

def getIsAdmin(self):
    isAdmin = None
    while not isAdmin:
        isAdmin = input("¿Desea que el nuevo usuario sea Administrador? (s/n): ").lower()
        if "n" in isAdmin:
            return False
        elif "s" in isAdmin:
            return True
        self.displayError(self.INVALID_INPUT)
    return isAdmin

def getExpression(self):
    #Clear the console
    print("--------------------------------------------------------------")
    print("Por favor ingrese la expresión E que desea calcular.")
    print("")
    return input("E = ")

# if result is None, it means that the expression is invalid
def displayResult(self, result=None):
    if result is None:
        self.displayError(self.INVALID_EXPRESSION)
        return print("--------------------------------------------------------------")
    print(f"\033[93mE = {result}\033[0m")
    print("----------------------------------")

#Prints the message in the console in orange color
def displayError(self, message):
    return print(f"\033[91m{message}\033[0m")

def displaySuccess(self, message):
    #Prints the message in the console in green color
    print(f"\033[92m{message}\033[0m")
    print("----------------------------------")

def displayWarning(self, message):
    #Prints the message in the console in yellow color
    print(f"\033[93m{message}\033[0m")
    print("----------------------------------")
    
def help():
    print("--------------------------------------------------------------")
    print("Ayuda - Calculadora Peculiar")
    print("--------------------------------------------------------------")
    print("Esta es una calculadora que permite realizar operaciones matemáticas")
    print("con números escritos en letras.")
    print("- Puede usar los siguientes operadores: +, -, *, /")
    print("- Puede usar paréntesis para agrupar operaciones. No se permiten paréntesis anidados.")
    print("- Los números deben estar escritos en español con espacios entre cada numero y operador.")
    print("Ejemplo: 'tres * (dos + uno)'")
    print("--------------------------------------------------------------")

       

def calculate(self, expression):
    try:
        result = self.parser.parseExpression(expression)
        result = self.calculator.calculateExpression(result)
        self.view.displayResult(result)
        logAddEntry(self.session.userId, Log.CALCULATION, True)
    except Exception as e:
        self.view.displayError(View.INVALID_EXPRESSION)
        logAddEntry(self.session.userId, Log.F_CALCULATION, False)
        
def createUser(self):
    isAdmin = self.view.getIsAdmin()
    idEntered = self.view.getNewUsername()
    try:
        if self.usersManager.createUser(idEntered, self.view.getNewPassword(), isAdmin):
            self.view.displaySuccess(View.USER_CREATED)
            logAddEntry(self.session.userId, Log.CREATE+". Nuevo Usuario: "+ idEntered, True)
    except Exception as e:
        self.view.displayError(View.USER_NOT_CREATED)
        logAddEntry(self.session.userId, Log.F_CREATE, False)

def createFirstUser():
    idEntered = getNewUsername()
    try:
        if createUser(idEntered, self.view.getNewPassword(), True):
            .displaySuccess(View.USER_CREATED)
            logAddEntry("N/A", Log.CREATE+". Primer Usuario Administrador: "+ idEntered, True)
    except Exception as e:
        self.view.displayError(View.USER_NOT_CREATED)
        logAddEntry(self.session.userId, Log.F_CREATE, False)

def validateFile() -> bool:
    try:
        with open(usersArchive, "r") as file:
            return True
    except FileNotFoundError:
        with open(usersArchive, "w") as file:
            pass
        return False
        
def logAddEntry( userId: str, entryType: str, success: bool):
    try:
        with open(usersArchive, "a", encoding='utf-8') as file:
            file.write(f"{datetime.now(timezone.utc)}   {SUCCESS if success else ERROR }   {entryType}   {userId}\n")
        return True
    except Exception as e:
        return False
        
def createUser(userId: str, password: str, isAdministrator: bool) -> bool:
    if isUser(userId):
        # throw exception 
        raise ValueError("User already exists")
    try:
        with open(usersArchive, "a") as file:
            file.write(f"{userId},{hashString(password)},{isAdministrator}\n")
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        return False
    
def validateUser(self, userId: str, password: str) -> bool:
    try:
        with open(self.usersArchive, "r") as file:
            for line in file:
                user, passw, isAdmin = line.strip().split(",")
                if user == userId and Hasher.validateString(password, passw):
                    return True
        return False
    except Exception as e:
        print(f"Error validating user: {e}")
        return False

def isUser(self, userId: str) -> bool:
    try:
        with open(self.usersArchive, "r") as file:
            for line in file:
                user, passw, isAdmin = line.strip().split(",")
                if user == userId:
                    return True
        return False
    except Exception as e:
        print(f"Error checking user existence: {e}")
        return False

def isAdmin(userId: str) -> bool:
    try:
        with open(usersArchive, "r") as file:
            for line in file:
                user, passw, isAdmin = line.strip().split(",")
                if user == userId:
                    return isAdmin.strip() == "True"
        return False
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False