import getpass

class View:
    def __init__(self):
        pass

    def display(self, message):
        print(message)

    def getInput(self, prompt):
        return input(prompt)
    
    def showMenuAdmin(self):
        print("1. Calculate Expression")
        print("2. Create User")
        print("3. Exit")
        return self.getInput("Select an option: ")
    
    def showMenuUser(self):
        print("1. Calculate Expression")
        print("2. Exit")
        return self.getInput("Select an option: ")
    
    def getInput(self, prompt):
        return input(prompt)
    
    def getInputPassword(self, prompt):
        # Use getpass to securely get password input without echoing it
        return getpass.getpass(prompt)
    