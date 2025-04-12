import bcrypt

class Hasher :
    """
    A class to hash strings using bcrypt.
    """
    @staticmethod
    def hashString(string: str) -> str:
        # Crear hash de la contraseña
        hashed = bcrypt.hashpw(string.encode(), bcrypt.gensalt())
        return hashed.decode()
    
    def validateString(string: str, hashed: str) -> bool:
        return bcrypt.checkpw(string.encode(), hashed.encode())
