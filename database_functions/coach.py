from entity_instances.coach_in import CoachIn
from create_tables import CREATE_COACH_TABLE
from insert_tables import INSERT_COACH
from select_tables import SELECT_COACH_ID_FROM_USERNAME


class Coach:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_COACH_TABLE)

    def add_coach(self, coach: CoachIn):
        with self.connection:
            self.cursor.execute(SELECT_COACH_ID_FROM_USERNAME, (coach.username,))
            coach.memberID = self.cursor.fetchone()[0]
            self.cursor.execute(INSERT_COACH, (coach.memberID,))

    