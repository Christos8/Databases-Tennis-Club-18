from entity_instances.coach_in import CoachIn
from create_tables import CREATE_COACH_TABLE
from insert_tables import INSERT_COACH


class Coach:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_COACH_TABLE)

    def add_coach(self, coach: CoachIn):
        with self.connection:
            self.cursor.execute(INSERT_COACH, (coach.memberID))

    