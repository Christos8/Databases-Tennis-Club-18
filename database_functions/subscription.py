from entity_instances.subscription_in import SubscriptionIn
from create_tables import CREATE_SUBSCRIPTION_TABLE
from insert_tables import INSERT_SUBSCRIPTION


class Subscription:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_SUBSCRIPTION_TABLE)

    def add_subscription(self, subscription: SubscriptionIn):
        with self.connection:
            self.cursor.execute(INSERT_SUBSCRIPTION, (subscription.id, subscription.startDate, subscription.endDate, subscription.type, subscription.category, subscription.status))

    