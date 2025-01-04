from entity_instances.lesson_in import LessonIn
from create_tables import CREATE_LESSON_TABLE
from insert_tables import INSERT_LESSON
from select_tables import SELECT_LESSONS


class Lesson:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_LESSON_TABLE)

    
    def return_lesson(self, coachid):
        self.cursor.execute(SELECT_LESSONS, (coachid,))
        lessons = self.cursor.fetchall()
    
        if not lessons:
            print("No lessons found.")
            return None
    
        lesson_objects = [LessonIn(*lesson) for lesson in lessons]
        return lesson_objects
    
    def add_lesson(self, lesson: LessonIn):
        with self.connection:
            self.cursor.execute(INSERT_LESSON, (lesson.id, lesson.date, lesson.startTime, lesson.endTime, lesson.difficulty, lesson.coachID))

    