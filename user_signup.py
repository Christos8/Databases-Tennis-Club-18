from entity_instances.user_auth_in import UserAuthIn
from create_tables import CREATE_USER_AUTH_TABLE
from insert_tables import INSERT_USER_AUTH


class SignUp:
    def __init__(self, username, cursor, connection):
        self.username = username
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_USER_AUTH_TABLE)


    def check_username(self, user: UserAuthIn):
        # placeholder for the actual username check logic
        if (self.username == "giorgis"):
            print("!Username already exists. Please try again.!")
            return False
        
        if (self.username == user.username):
            print("!Username already exists. Please try again.!")
            return False
        return True

    def user_signup(self, password, username, user: UserAuthIn):
        # placeholder for the actual signup logic
        with self.connection:
            self.cursor.execute(INSERT_USER_AUTH, (self.username, self.password))

        print(f"User {self.username} signed up successfully with password {password}.")