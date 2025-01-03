from entity_instances.player_in import PlayerIn
from create_tables import CREATE_PLAYER_TABLE
from insert_tables import INSERT_PLAYER
from select_tables import SELECT_MEMBER_ID_FROM_USERNAME, SELECT_PLAYER_ID_FROM_MEMBER_ID


class Player:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_PLAYER_TABLE)

    def check_player_exists(self, username):
        with self.connection:
            self.cursor.execute(SELECT_MEMBER_ID_FROM_USERNAME, (username,))
            result = self.cursor.fetchone()
            if result != None:
                self.cursor.execute(SELECT_PLAYER_ID_FROM_MEMBER_ID, (result[0],))
                result = self.cursor.fetchone()
                if result != None:
                    return True
            return False


    def add_player(self, player: PlayerIn):
        with self.connection:
            self.cursor.execute(SELECT_MEMBER_ID_FROM_USERNAME, (player.username,))
            player.memberID = self.cursor.fetchone()[0]
            self.cursor.execute(INSERT_PLAYER, (player.memberID,))

    