# from entity_instances.player_sub_in import PlayerSubscriptionIn
# from create_tables import CREATE_PLAYER_SUBSCRIPTION_TABLE
# from insert_tables import INSERT_PLAYER_SUBSCRIPTION
# from select_tables import SELECT_ACTIVE_SUBSCRIPTION

# class PlayerSub:
#     def __init__(self, cursor, connection):
#         self.cursor = cursor
#         self.connection = connection
#         self.cursor.executescript(CREATE_PLAYER_SUBSCRIPTION_TABLE)

#     def add_player_sub(self, playersub: PlayerSubscriptionIn):
#         with self.connection:
#             self.cursor.execute(INSERT_PLAYER_SUBSCRIPTION, (playersub.playerID, playersub.subscriptionID))

#     def check_subscription(self, playerID):
#         self.cursor.execute(SELECT_ACTIVE_SUBSCRIPTION , (playerID,))
#         return self.cursor.fetchone() is not None


    