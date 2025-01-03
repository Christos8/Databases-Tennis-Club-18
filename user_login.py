import bcrypt
from entity_instances.user_auth_in import UserAuthIn
from __init__ import user_functions, player_functions

class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    # Returns True if the login is successful, false otherwise
    def login(self):
        if not player_functions.check_player_exists(self.username):
            return False
        if bcrypt.checkpw(self.password.encode(), user_functions.return_hashed_password(self.username).encode()):
                return True
        return False
