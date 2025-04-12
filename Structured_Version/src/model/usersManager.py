from utils.hasher import Hasher

class UsersManager : 
    def __init__(self):
        self.usersArchive = "data/users.dbfile"

    def validateFile(self) -> bool:
        try:
            with open(self.usersArchive, "r") as file:
                return True
        except FileNotFoundError:
            with open(self.usersArchive, "w") as file:
                pass
            return False
        
    def createUser(self, userId: str, password: str, isAdministrator: bool) -> bool:
        if self.isUser(userId):
            # throw exception 
            raise ValueError("User already exists")
        try:
            with open(self.usersArchive, "a") as file:
                file.write(f"{userId},{Hasher.hashString(password)},{isAdministrator}\n")
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
    
    def isAdmin(self, userId: str) -> bool:
        try:
            with open(self.usersArchive, "r") as file:
                for line in file:
                    user, passw, isAdmin = line.strip().split(",")
                    if user == userId:
                        return isAdmin.strip() == "True"
            return False
        except Exception as e:
            print(f"Error checking admin status: {e}")
            return False