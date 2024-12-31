from entity_instances.player_in import PlayerIn
from create_tables import CREATE_PLAYER_TABLE
from insert_tables import INSERT_PLAYER


class Player:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_PLAYER_TABLE)

    def add_player(self, player: PlayerIn):
        with self.connection:
            self.cursor.execute(INSERT_PLAYER, (player.memberID))

    