class Session:
    def __init__(self, userId: str, isAdministrator: bool):
        self.userId = userId
        self.isAdministrator = isAdministrator
        
        