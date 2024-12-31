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
    ):
        self.id = id
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.difficulty = ( difficulty
                             or fake.random_choices(
                                 elements=[
                                     "Amateur",
                                     "Intermediate",
                                     "Professional"
                                 ],
                                 length = 1,
                             ).pop()
        )
        self.coachID = coachID
        

