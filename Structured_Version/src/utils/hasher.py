import bcrypt

class Hasher :
    """
    A class to hash strings using SHA-256.
    """

    @staticmethod
    def hashString(string: str) -> str:
        # Crear hash de la contraseña
        password = string.encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed.decode()
    
    def validateString(self, string: str, hashed: str) -> bool:
        return bcrypt.checkpw(string, hashed.encode())
