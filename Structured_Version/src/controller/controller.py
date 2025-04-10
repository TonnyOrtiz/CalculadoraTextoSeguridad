import sys
from model.parser import Parser

class Controller:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.parser = Parser()
        self.args = sys.argv[1:]
        self.argc = len(self.args)

    def run(self):
        while True:
            self.vista.mostrar_tareas(self.modelo.obtener_tareas())
            nueva = self.vista.pedir_nueva_tarea()
            if nueva.lower() in ['salir', 'exit']:
                self.vista.mostrar_mensaje("¡Adiós!")
                break
            self.modelo.agregar_tarea(nueva)