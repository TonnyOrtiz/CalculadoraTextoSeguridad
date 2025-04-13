import os
from utils.hasher import Hasher

class UsersManager : 
    USERSFILE = "Structured_Version/data/users.dbfile"

    def validateFile() -> bool:
        try:
            with open(UsersManager.USERSFILE, "r") as file:
                # Check if the file is empty
                if os.stat(UsersManager.USERSFILE).st_size == 0:
                    return False
                return True
        except FileNotFoundError:
            os.makedirs(os.path.dirname(UsersManager.USERSFILE), exist_ok=True)
            with open(UsersManager.USERSFILE, "w") as file:
                pass
            return False
        
    def createUser(userId: str, password: str, isAdministrator: bool) -> bool:
        if UsersManager.isUser(userId):
            # throw exception 
            raise ValueError("User already exists")
        try:
            with open(UsersManager.USERSFILE, "a") as file:
                file.write(f"{userId},{Hasher.hashString(password)},{isAdministrator}\n")
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def validateUser(userId: str, password: str) -> bool:
        try:
            with open(UsersManager.USERSFILE, "r") as file:
                for line in file:
                    user, passw, isAdmin = line.strip().split(",")
                    if user == userId and Hasher.validateString(password, passw):
                        return True
            return False
        except Exception as e:
            print(f"Error validating user: {e}")
            return False
    
    def isUser(userId: str) -> bool:
        try:
            with open(UsersManager.USERSFILE, "r") as file:
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
            with open(UsersManager.USERSFILE, "r") as file:
                for line in file:
                    user, passw, isAdmin = line.strip().split(",")
                    if user == userId:
                        return isAdmin.strip() == "True"
            return False
        except Exception as e:
            print(f"Error checking admin status: {e}")
            return False