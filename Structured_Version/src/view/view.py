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
    USER_FILE_NOT_FOUND = "El archivo de usuarios no existe, \nesta puede ser la primera vez que se ejecuta el programa. \nSe creará un nuevo archivo de usuario."
    INVALID_OPTION = "Opción inválida. Por favor, seleccione una opción válida."

    # Success messages
    USER_CREATED = "Usuario creado exitosamente."

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
        return View.getInput("Ingrese su opción: ")
    
    def showMenuUser():
        print("Menu de la Calculadora Peculiar")
        print("-----------------------------------")
        print("Por favor, seleccione una opción del menú:")
        print("1.Calcular expresión matemática con números en letras")
        print("0. Salir")
        print("")
        return View.getInput("Ingrese el número de opción: ")
    
    def getUsername():
        idEntered = None
        while not idEntered:
            idEntered = input("Ingrese su ID de usuario: ")
            if idEntered:
                return idEntered
            View.displayError(View.EMPTY_USERNAME)
                
    def getPassword():
        return getpass.getpass("Ingrese su contraseña: ")
    
    def getNewPassword():
        temp =getpass.getpass("Ingrese la nueva contraseña: ")
        if temp == getpass.getpass("Confirme la nueva contraseña: "):
            return temp
        View.displayError(View.PASSWORD_MISMATCH)
        
    def getNewUsername():
        idEntered = None
        while not idEntered:
            idEntered = input("Ingrese el nuevo ID de usuario: ")
            if idEntered:
                return idEntered
            View.displayError(View.EMPTY_USERNAME)

    def getIsAdmin():
        isAdmin = None
        while not isAdmin:
            isAdmin = input("¿Desea que el nuevo usuario sea Administrador? (s/n): ").lower()
            if "n" in isAdmin:
                return False
            elif "s" in isAdmin:
                return True
            View.displayError(View.INVALID_INPUT)
        return isAdmin
    
    def getExpression():
        #Clear the console
        print("--------------------------------------------------------------")
        print("Por favor ingrese la expresión E que desea calcular.")
        print("")
        return input("E = ")
    
    # if result is None, it means that the expression is invalid
    def displayResult(result=None):
        if result is None:
            View.displayError(View.INVALID_EXPRESSION)
            return print("--------------------------------------------------------------")
        print(f"\033[93mE = {result}\033[0m")
        print("----------------------------------")
    
    #Prints the message in the console in orange color
    def displayError(message):
        return print(f"\033[91m{message}\033[0m")
    
    def displaySuccess(message):
        #Prints the message in the console in green color
        print(f"\033[92m{message}\033[0m")
        print("----------------------------------")

    def displayWarning(message):
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