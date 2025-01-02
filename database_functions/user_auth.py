from entity_instances.user_auth_in import UserAuthIn
from create_tables import CREATE_USER_AUTH_TABLE
from insert_tables import INSERT_USER_AUTH

class UserAuth:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_USER_AUTH_TABLE)
        
    def add_user_auth(self, user_auth: UserAuthIn):
        with self.connection:
            self.cursor.execute(INSERT_USER_AUTH, (user_auth.username, user_auth.password))