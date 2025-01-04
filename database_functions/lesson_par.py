from entity_instances.lesson_par_in import LessonParticipationIn
from create_tables import CREATE_LESSON_PARTICIPATION_TABLE
from insert_tables import INSERT_LESSON_PARTICIPATION
from select_tables import SELECT_LESSON_PARTICIPATION


class LessonPar:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_LESSON_PARTICIPATION_TABLE)

    def add_lesson_par(self, lessonpar: LessonParticipationIn):
        with self.connection:
            self.cursor.execute(INSERT_LESSON_PARTICIPATION, (lessonpar.playerID, lessonpar.lessonID))

    def check_participation(self, lessonpar: LessonParticipationIn):
        self.cursor.execute(SELECT_LESSON_PARTICIPATION , (lessonpar.playerID, lessonpar.lessonID))
        return self.cursor.fetchone() is not None

    