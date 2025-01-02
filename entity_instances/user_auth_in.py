import bcrypt

class UserAuthIn:

    def __init__(
        self,
        username = None,
        password = None,
    ):
        
        self.username = username        
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')