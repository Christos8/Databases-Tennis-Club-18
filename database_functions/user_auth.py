from entity_instances.user_auth_in import UserAuthIn
from create_tables import CREATE_USER_AUTH_TABLE
from insert_tables import INSERT_USER_AUTH
from select_tables import SELECT_USERNAME_FROM_USER_AUTH, SELECT_PASSWORD_FROM_USER_AUTH

class UserAuth:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_USER_AUTH_TABLE)

    def check_username(self, username):
        with self.connection:
            self.cursor.execute(SELECT_USERNAME_FROM_USER_AUTH, (username,))
            if self.cursor.fetchone():
                return True
            return False
    
    def check_password(self, username, password):
        with self.connection:
            self.cursor.execute(SELECT_PASSWORD_FROM_USER_AUTH, (username,))
            if self.cursor.fetchone()[0] == password:
                return True
            return False
        
    def add_user_auth(self, user_auth: UserAuthIn):
        with self.connection:
            self.cursor.execute(INSERT_USER_AUTH, (user_auth.username, user_auth.password))