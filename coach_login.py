import bcrypt

class CoachLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if (self.username != "chris"): # select_user(self.username)
            return False
        #check if the password is 1234 but encrypted
        
        _1234 = '1234'
        hashedpw = bcrypt.hashpw(_1234.encode(), bcrypt.gensalt())
        
        if(not (bcrypt.checkpw(self.password.encode(), hashedpw))):
            return False
        # placeholder for the actual login logic
        if (bcrypt.checkpw(self.password.encode(), hashedpw) and self.username == "chris"):
            return True