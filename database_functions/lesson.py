from entity_instances.lesson_in import LessonIn
from create_tables import CREATE_LESSON_TABLE
from insert_tables import INSERT_LESSON
from select_tables import SELECT_ALL_LESSONS


class Lesson:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_LESSON_TABLE)

    def add_lesson(self, lesson: LessonIn):
        with self.connection:
            self.cursor.execute(INSERT_LESSON, (lesson.id, lesson.date, lesson.startTime, lesson.endTime, lesson.difficulty, lesson.coachID))

    def return_lesson(self):
        self.cursor.execute(SELECT_ALL_LESSONS)
        _, *lesson_data = self.cursor.fetchall()
        lesson = LessonIn(*lesson_data)
        return lesson