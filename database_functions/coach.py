from entity_instances.coach_in import CoachIn
from create_tables import CREATE_COACH_TABLE
from insert_tables import INSERT_COACH
from select_tables import SELECT_COACH_ID_FROM_MEMBER_ID, SELECT_MEMBER_ID_FROM_USERNAME, SELECT_PLAYER_ID_FROM_MEMBER_ID


class Coach:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_COACH_TABLE)

    def check_coach_exists(self, username):
        with self.connection:
            self.cursor.execute(SELECT_MEMBER_ID_FROM_USERNAME, (username,))
            result = self.cursor.fetchone()
            if result != None:
                self.cursor.execute(SELECT_COACH_ID_FROM_MEMBER_ID, (result[0],))
                result = self.cursor.fetchone()
                if result != None:
                    return True
            return False

    def add_coach(self, coach: CoachIn):
        with self.connection:
            self.cursor.execute(SELECT_MEMBER_ID_FROM_USERNAME, (coach.username,))
            coach.memberID = self.cursor.fetchone()[0]
            self.cursor.execute(INSERT_COACH, (coach.memberID,))

    