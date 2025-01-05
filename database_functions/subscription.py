from entity_instances.subscription_in import SubscriptionIn
from create_tables import CREATE_SUBSCRIPTION_TABLE
from insert_tables import INSERT_SUBSCRIPTION
from select_tables import SELECT_ACTIVE_SUBSCRIPTION


class Subscription:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_SUBSCRIPTION_TABLE)

    def add_subscription(self, subscription: SubscriptionIn):
        with self.connection:
            self.cursor.execute(INSERT_SUBSCRIPTION, (subscription.startDate, subscription.endDate, subscription.type, subscription.category, subscription.status, subscription.playerID))

    def check_subscription(self, playerID):
        self.cursor.execute(SELECT_ACTIVE_SUBSCRIPTION , (playerID,))
        return self.cursor.fetchone() is not None