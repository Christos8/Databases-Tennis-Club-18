from entity_instances.lesson_in import LessonIn
from create_tables import CREATE_LESSON_TABLE
from insert_tables import INSERT_LESSON
from select_tables import SELECT_LESSONS, SELECT_ALL_LESSONS, SELECT_LESSONID, SELECT_LESSON_FROM_ID


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
            self.cursor.execute(INSERT_LESSON, (lesson.date, lesson.startTime, lesson.endTime, lesson.difficulty, lesson.coachID, lesson.fieldid))

    
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
                  Field: {lesson[5]}
                  Coach: {lesson[6]}
                  """)   
            
    
    def get_lesson_id(self, fieldid, date, starttime, endtime, coachid):
        self.fieldid = fieldid
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.coachid = coachid
        self.cursor.execute(SELECT_LESSONID, (self.fieldid, self.date, self.starttime, self.endtime, self.coachid))
        self.lessonid = self.cursor.fetchone()[0]
        return self.lessonid
    
    def get_lesson_from_id(self, lessonid):
        self.cursor.execute(SELECT_LESSON_FROM_ID, (lessonid,))
        lesson = self.cursor.fetchone()
        return LessonIn(*lesson)