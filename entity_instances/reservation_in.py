
class ReservationIn:
    def __init__(
        self,
        id = None,
        fieldID = None,
        startTime = None,
        endTime = None,
        lessonID = None,
        coachID = None
    ):
        self.id = id
        self.fieldID = fieldID
        self.startTime = startTime
        self.endTime = endTime
        self.lessonID = lessonID
        self.coachID = coachID
        