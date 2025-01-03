import bcrypt
from entity_instances.user_auth_in import UserAuthIn
from __init__ import user_functions, member_functions

class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        UserAuthIn(username, password)
    

    def login(self):
        if (user_functions.check_username(self.username)):
            print("!Username does not exist. Please try again.!")
        if(user_functions.check_password(self.username, self.password)):
            print("!Password does not match. Please try again.!")
        else:
            return False