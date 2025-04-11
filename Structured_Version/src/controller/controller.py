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

    def run(self):
        userId = self.view.getInput("Ingrese su nombre de usuario: ")
        password = self.view.getInputPassword("Ingrese su contraseña: ")
        if not self.usersManager.validateUser(userId, password) :
            self.view.display("Usuario o contraseña incorrectos. Intente de nuevo.")
            return
        else:
            self.view.display("Inicio de sesión exitoso.")
            self.session = Session(userId, self.usersManager.isAdmin(userId))
            
        while True:
            if self.session.isAdministrator:
                option = self.view.showMenuAdmin()
                
                if option == "1":
                    expression = self.view.getInput("Ingrese la expresión: ")
                    try:
                        result = self.parser.parseExpression(expression)
                        result = self.calculator.calculateExpression(result)
                        self.view.display(f"Resultado: {result}")
                    except Exception as e:
                        self.view.display(f"Error al procesar la expresión: {e}")
                    
                if option == "2":
                    userId = self.view.getInput("Ingrese el ID del nuevo usuario: ")
                    password = self.view.getInputPassword("Ingrese la contraseña del nuevo usuario: ")
                    isAdmin = self.view.getInput("¿Es administrador? (s/n): ").lower() == "s"
                    try:
                        if self.usersManager.createUser(userId, password, isAdmin):
                            self.view.display("Usuario creado exitosamente.")
                            continue
                    except Exception as e:
                        self.view.display(f"Error al crear el usuario: {e}")
                    
                if option == "3":
                    self.view.display("¡Adiós!")
                    break
            else:
                option = self.view.showMenuUser()
                
                if option == "1":
                    expression = self.view.getInput("Ingrese la expresión: ")
                    try:
                        result = self.parser.parseExpression(expression)
                        result = self.calculator.calculateExpression(result)
                        self.view.display(f"Resultado: {result}")
                    except Exception as e:
                        self.view.display(f"Error al procesar la expresión: {e}")
                        
                if option == "2":
                    self.view.display("¡Adiós!")
                    break
            