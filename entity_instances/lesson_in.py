from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")


class LessonIn:
    def __init__(
        self,
        id	= None,
        date = None,
        startTime = None,
        endTime = None,
        difficulty = None,
        coachID = None,
        fieldid = None,
    ):
        self.id = id
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.difficulty = difficulty
        self.coachID = coachID
        self.fieldid = fieldid
        

