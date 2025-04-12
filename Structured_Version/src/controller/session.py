class Session:
    userId: str
    isAdministrator: bool
    def __init__(self, userId: str, isAdministrator: bool):
        self.userId = userId
        self.isAdministrator = isAdministrator
        
        