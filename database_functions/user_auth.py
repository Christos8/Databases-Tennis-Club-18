from entity_instances.user_auth_in import UserAuthIn
from create_tables import CREATE_USER_AUTH_TABLE
from insert_tables import INSERT_USER_AUTH
from select_tables import SELECT_USERNAME_FROM_USER_AUTH, SELECT_PASSWORD_FROM_USER_AUTH

class UserAuth:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_USER_AUTH_TABLE)

#returns True if the username exists in the database
    def check_username(self, username):
        with self.connection:
            self.cursor.execute(SELECT_USERNAME_FROM_USER_AUTH, (username,))
            if self.cursor.fetchone():
                return True
            return False
    
#returns the hashed password of the given username
    def return_hashed_password(self, username):
        with self.connection:
            self.cursor.execute(SELECT_PASSWORD_FROM_USER_AUTH, (username,))
            return self.cursor.fetchone()[0]

    def add_user_auth(self, user_auth: UserAuthIn):
        with self.connection:
            self.cursor.execute(INSERT_USER_AUTH, (user_auth.username, user_auth.password))