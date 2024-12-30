from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")


class LESSON_IN:
    def __init__(
        self,
        ID	= None,
        Date = None,
        StartTime = None,
        EndTime = None,
        Difficulty = None,
        CoachID = None,
    ):
        self.ID = ID
        self.Date = Date
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.Difficulty = ( Difficulty
                             or fake.random_choices(
                                 elements=[
                                     "Amateur",
                                     "Intermediate",
                                     "Professional"
                                 ],
                                 length = 1,
                             ).pop()
        )
        self.CoachID = CoachID
        

