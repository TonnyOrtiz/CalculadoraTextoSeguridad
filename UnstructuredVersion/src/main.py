import getpass, sys, os
from datetime import datetime, timezone
import bcrypt 

# Constants ---------------------------------------------------
# File paths
usersArchive = "UnstructuredVersion/data/users.dbfile"
logArchive = "UnstructuredVersion/data/filehistory.log"

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

# Parser Constants
WORD_TO_NUMBER = {
    "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
    "once": 11, "doce": 12, "trece": 13, "catorce": 14,
    "quince": 15, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18,
    "diecinueve": 19, "veinte": 20
}
TENS_TO_NUMBER = {
    "treinta": 30, "cuarenta": 40, "cincuenta": 50,
    "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
}
TWENTY_WORD = "veinti"
TWENTY_NUMBER = 20
OPERATORS = ["+", "-", "*", "/"]
PARENTHESES = ["(", ")"]

# Variables ---------------------------------------------------
sessionId = None
sessionIsAdmin = False

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
        displayError(EMPTY_USERNAME)

def getIsAdmin():
    isAdmin = None
    while not isAdmin:
        isAdmin = input("¿Desea que el nuevo usuario sea Administrador? (s/n): ").lower()
        if "n" in isAdmin:
            return False
        elif "s" in isAdmin:
            return True
        displayError(INVALID_INPUT)
    return isAdmin

def getExpression():
    #Clear the console
    print("--------------------------------------------------------------")
    print("Por favor ingrese la expresión E que desea calcular.")
    print("")
    return input("E = ")

# if result is None, it means that the expression is invalid
def displayResult( result=None):
    if result is None:
        displayError(INVALID_EXPRESSION)
        return print("--------------------------------------------------------------")
    print(f"\033[93mE = {result}\033[0m")
    print("----------------------------------")

#Prints the message in the console in orange color
def displayError( message):
    return print(f"\033[91m{message}\033[0m")

def displaySuccess( message):
    #Prints the message in the console in green color
    print(f"\033[92m{message}\033[0m")
    print("----------------------------------")

def displayWarning( message):
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

       
def calculate( expression):
    try:
        result = parseExpression(expression)
        result = calculateExpression(result)
        displayResult(result)
        logAddEntry(sessionId, CALCULATION, True)
    except Exception as e:
        displayError(INVALID_EXPRESSION)
        logAddEntry(sessionId, F_CALCULATION, False)

def validateFile() -> bool:
    try:
        with open(usersArchive, "r") as file:
            return True
    except FileNotFoundError:
        os.makedirs(os.path.dirname(usersArchive), exist_ok=True)
        with open(usersArchive, "w") as file:
            pass
        return False
        
def logAddEntry( userId: str, entryType: str, success: bool):
    try:
        with open(logArchive, "a", encoding='utf-8') as file:
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
            file.write(f"{userId},{bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()},{isAdministrator}\n")
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        return False
    
def validateUser(userId: str, password: str) -> bool:
    try:
        with open(usersArchive, "r") as file:
            for line in file:
                user, passw, isAdmin = line.strip().split(",")
                if user == userId and bcrypt.checkpw(password.encode(), passw.encode()):
                    return True
        return False
    except Exception as e:
        print(f"Error validating user: {e}")
        return False

def isUser( userId: str) -> bool:
    try:
        with open(usersArchive, "r") as file:
            for line in file:
                user, passw, isAdmin = line.strip().split(",")
                if user == userId:
                    return True
        return False
    except Exception as e:
        print(f"Error checking user existence: {e}")
        return False

def validateIsAdmin(userId: str) -> bool:
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
    
def parseExpression(expression: str) -> list:
    try:
        
        return wordToNum(expression)
    except Exception as e:
        raise ValueError(f"Invalid expression: {expression}") from e

def wordToNum(expression):
    # Preprocess the expression to add spaces around parentheses
    for p in PARENTHESES:
        expression = expression.replace(p, f" {p} ")

    # Add spaces around operators if not already spaced
    for op in OPERATORS:
        expression = expression.replace(op, f" {op} ")

    # Add spaces around "y" (and) for compound numbers
    expression = expression.replace("y", " y ")
    
    # Split the expression into words.
    words = expression.split()
    tokens = []  # List to store the parsed tokens
    i = 0

    while i < len(words):
        word = words[i]
        if word in WORD_TO_NUMBER:
            tokens.append(WORD_TO_NUMBER[word])
        elif word.startswith(TWENTY_WORD) and len(word) > 6:
            base = TWENTY_NUMBER
            suffix = word[6:]
            if suffix in WORD_TO_NUMBER:
                tokens.append(base + WORD_TO_NUMBER[suffix])
        elif word in TENS_TO_NUMBER:
            # Check for compound numbers like "cuarenta y dos"
            if i + 2 < len(words) and words[i + 1] == "y" and words[i + 2] in WORD_TO_NUMBER:
                tokens.append(TENS_TO_NUMBER[word] + WORD_TO_NUMBER[words[i + 2]])
                i += 2  # Skip "y" and the unit word
            else:
                tokens.append(TENS_TO_NUMBER[word])
        elif word in OPERATORS:
            tokens.append(word)
        elif word in PARENTHESES:
            tokens.append(word)
        else:
            raise ValueError(f"Unknown word in expression: {word}")
        i += 1

    return tokens  # Return the list of tokens

def calculateExpression(tokens: list) -> float:
    try:    
        result = evaluateTokens(tokens)
        return result
    except Exception as e:
        raise ValueError(f"Invalid expression: {tokens}") from e
    
def evaluateTokens(tokens: list) -> float:
    # Handle parentheses first
    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] == "(":
            # Find the matching closing parenthesis
            open_index = i
            close_index = i + 1
            depth = 1
            while close_index < len(tokens) and depth > 0:
                if tokens[close_index] == "(":
                    depth += 1
                elif tokens[close_index] == ")":
                    depth -= 1
                close_index += 1

            if depth != 0:
                raise ValueError("Mismatched parentheses")

            # Evaluate the expression inside the parentheses
            inner_result = evaluateTokens(tokens[open_index + 1 : close_index - 1])

            # Replace the parentheses and their contents with the result
            tokens = tokens[:open_index] + [inner_result] + tokens[close_index:]
            i = open_index  # Reset index to the position of the result
        else:
            i += 1

    # Handle multiplication and division first
    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] in ("*", "/"):
            if tokens[i] == "*":
                result = (tokens[i - 1]) * (tokens[i + 1])
            elif tokens[i] == "/":
                if tokens[i + 1] == 0:
                    raise ValueError("Cannot divide by zero")
                result = (tokens[i - 1]) / (tokens[i + 1])

            # Replace the operator and its operands with the result
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
            i -= 1  # Adjust index after modifying the list
        else:
            i += 1

    # Handle addition and subtraction
    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] in ("+", "-"):
            if tokens[i] == "+":
                result = (tokens[i - 1]) + (tokens[i + 1])
            elif tokens[i] == "-":
                result = (tokens[i - 1]) - (tokens[i + 1])

            # Replace the operator and its operands with the result
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
            i -= 1  # Adjust index after modifying the list
        else:
            i += 1

    # The final result will be the only element left in the tokens list
    return tokens[0]

def main():
    if not validateFile():
        displayWarning(USER_FILE_NOT_FOUND)
        logAddEntry("N/A", USER_FILE, True)
        idEntered = getNewUsername()
        try:
            if createUser(idEntered, getNewPassword(), True):
                displaySuccess(USER_CREATED)
                logAddEntry("N/A", CREATE+". Primer Usuario Administrador: "+ idEntered, True)
        except Exception as e:
            displayError(USER_NOT_CREATED)
            logAddEntry(sessionId, F_CREATE, False)
    try:
        idEntered = getUsername()
        password = getPassword()
        if not validateUser(idEntered, password) :
            displayError(INVALID_AUTH)
            logAddEntry("N/A" , F_LOGIN, False)
        else:
            sessionId = idEntered
            sessionIsAdmin=validateIsAdmin(idEntered)
            logAddEntry(sessionId, LOGIN, True)
            while sessionId:
                if sessionIsAdmin:
                    option = showMenuAdmin()
                    if option == "1":
                        calculate(getExpression())
                    elif option == "2":
                        isAdmin = getIsAdmin()
                        idEntered = getNewUsername()
                        try:
                            if createUser(idEntered, getNewPassword(), isAdmin):
                                displaySuccess(USER_CREATED)
                                logAddEntry(sessionId, CREATE+". Nuevo Usuario: "+ idEntered, True)
                        except Exception as e:
                            displayError(USER_NOT_CREATED)
                            logAddEntry(sessionId, F_CREATE, False)
                    elif option == "0":
                        display("¡Adiós!")
                        logAddEntry(sessionId, LOGOUT, True)
                        sessionId = None
                    else:
                        displayError(INVALID_MENU_OPTION)
                        display("---------------------------------------------------------------")
                else:
                    option = showMenuUser()     
                    if option == "1":
                        calculate(getExpression())
                    elif option == "0":
                        display("¡Adiós!")
                        logAddEntry(sessionId, LOGOUT, True)
                        sessionId= None
                    else:
                        displayError(INVALID_MENU_OPTION)
                        display("---------------------------------------------------------------")
    except KeyboardInterrupt:
        displayWarning("\nInterrumpido por el usuario.")
        logAddEntry(sessionId, KEYBOARD_INTERRUPT, True)
        sys.exit(0)
    except Exception as e:
        displayError(f"Error: {e}")
        logAddEntry(sessionId, F_LOGOUT, False)
        sys.exit(1)

if __name__ == "__main__":
    main()