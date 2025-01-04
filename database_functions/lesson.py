from entity_instances.lesson_in import LessonIn
from create_tables import CREATE_LESSON_TABLE
from insert_tables import INSERT_LESSON
from select_tables import SELECT_LESSONS, SELECT_ALL_LESSONS


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

    
    def display_lessons(self):

        self.cursor.execute(SELECT_ALL_LESSONS)
        lessons = self.cursor.fetchall()
        for lesson in lessons:
            print(f"""
                  Lesson ID: {lesson[0]}
                  Date: {lesson[1]}
                  Starting Time: {lesson[2]}
                  Ending Time: {lesson[3]}
                  Difficulty: {lesson[4]}
                  Coach: {lesson[5]}
                  """)   

    