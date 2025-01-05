# from entity_instances.player_reserv_in import PlayerReservationIn
# from create_tables import CREATE_PLAYER_RESERVATION_TABLE
# from insert_tables import INSERT_PLAYER_RESERVATION


# class PlayerRes:
#     def __init__(self, cursor, connection):
#         self.cursor = cursor
#         self.connection = connection
#         self.cursor.executescript(CREATE_PLAYER_RESERVATION_TABLE)

#     def add_player_res(self, playerres: PlayerReservationIn):
#         with self.connection:
#             self.cursor.execute(INSERT_PLAYER_RESERVATION, (playerres.playerID, playerres.reservationID))

    