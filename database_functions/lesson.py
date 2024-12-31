from entity_instances.lesson_in import LessonIn
from create_tables import CREATE_LESSON_TABLE
from insert_tables import INSERT_LESSON


class Lesson:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_LESSON_TABLE)

    def add_lesson(self, lesson: LessonIn):
        with self.connection:
            self.cursor.execute(INSERT_LESSON, (lesson.id, lesson.date, lesson.startTime, lesson.endTime, lesson.difficulty, lesson.coachID))

    