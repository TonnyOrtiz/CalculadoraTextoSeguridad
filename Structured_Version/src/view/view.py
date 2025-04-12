import getpass

class View:
    
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

    # Success messages
    USER_CREATED = "Usuario creado exitosamente."

    def __init__(self):
        pass

    def display(self, message):
        print(message)

    def getInput(self, prompt):
        return input(prompt)
    
    def showMenuAdmin(self):
        print("Menu de la Calculadora Peculiar")
        print("-----------------------------------")
        print("Por favor, seleccione una opción del menú:")
        print("1. Calcular expresión matemática con números en letras")
        print("2. Crear nuevo usuario")
        print("0. Salir")
        print("")
        return self.getInput("Ingrese su opción: ")
    
    def showMenuUser(self):
        print("Menu de la Calculadora Peculiar")
        print("-----------------------------------")
        print("Por favor, seleccione una opción del menú:")
        print("1.Calcular expresión matemática con números en letras")
        print("0. Salir")
        print("")
        return self.getInput("Ingrese el número de opción: ")
    
    def getUsername(self):
        idEntered = None
        while not idEntered:
            idEntered = input("Ingrese su ID de usuario: ")
            if idEntered:
                return idEntered
            self.view.displayError(self.view.EMPTY_USERNAME)
                
    def getPassword(self):
        return getpass.getpass("Ingrese su contraseña: ")
    
    def getNewPassword(self):
        temp =getpass.getpass("Ingrese la nueva contraseña: ")
        if temp == getpass.getpass("Confirme la nueva contraseña: "):
            return temp
        self.displayError(self.PASSWORD_MISMATCH)
        
    def getNewUsername(self):
        idEntered = None
        while not idEntered:
            idEntered = input("Ingrese el nuevo ID de usuario: ")
            if idEntered:
                return idEntered
            self.view.displayError(self.view.EMPTY_USERNAME)
    
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