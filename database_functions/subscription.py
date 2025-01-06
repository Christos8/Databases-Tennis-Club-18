from datetime import datetime 
from entity_instances.subscription_in import SubscriptionIn
from create_tables import CREATE_SUBSCRIPTION_TABLE
from insert_tables import INSERT_SUBSCRIPTION
from select_tables import SELECT_ACTIVE_SUBSCRIPTION, SELECT_SUBSCRIPTION_END_DATE
from update_tables import UPDATE_SUBSCRIPTION_STATUS


class Subscription:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_SUBSCRIPTION_TABLE)

    def add_subscription(self, subscription: SubscriptionIn):
        with self.connection:
            self.cursor.execute(INSERT_SUBSCRIPTION, (subscription.startDate, subscription.endDate, subscription.type, subscription.category, subscription.status, subscription.playerID))

    def update_subscription_status(self, playerID):
        self.cursor.execute(SELECT_SUBSCRIPTION_END_DATE, (playerID,))
        end_date = self.cursor.fetchone()
        if end_date:
            formatted_date = datetime.strptime(end_date[0], '%d/%m/%Y')  # Parse date in dd-mm-yyyy format
            current_date = datetime.today()
            if current_date > formatted_date:

                self.cursor.execute(UPDATE_SUBSCRIPTION_STATUS, (playerID,))
                self.connection.commit() 
                print("Subscription status updated for playerID:", playerID)

    def check_subscription(self, playerID):
        self.cursor.execute(SELECT_ACTIVE_SUBSCRIPTION, (playerID,))
        active_subscription = self.cursor.fetchone()
        if not active_subscription:
            print("No active subscription found for playerID:", playerID)
            return False
        else:
            self.update_subscription_status(playerID)
            self.cursor.execute(SELECT_ACTIVE_SUBSCRIPTION, (playerID,))
            return self.cursor.fetchone() is not None