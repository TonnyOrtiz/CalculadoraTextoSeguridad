from datetime import datetime, timezone
class Log : 
    ## This class is responsible for logging user actions and errors.

    # EntryTypes:
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

    # Log file:
    LOGFILE = "Structured_Version/data/history.log"
        
    def addEntry(userId: str, entryType: str, success: bool):
        try:
            with open(Log.LOGFILE, "a", encoding='utf-8') as file:
                file.write(f"{datetime.now(timezone.utc)}   {Log.SUCCESS if success else Log.ERROR }   {entryType}   {userId}\n")
            return True
        except Exception as e:
            return False