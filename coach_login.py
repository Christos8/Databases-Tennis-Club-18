import bcrypt
from __init__ import user_functions, coach_functions

class CoachLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if not coach_functions.check_coach_exists(self.username):
            return False
        if bcrypt.checkpw(self.password.encode(), user_functions.return_hashed_password(self.username).encode()):
                return True
        return False