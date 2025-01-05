
class ReservationIn:
    def __init__(
        self,
        id = None,
        playerid = None,
        fieldID = None,
        date = None,
        startTime = None,
        endTime = None,
        lessonID = None,
        coachID = None
    ):
        self.id = id
        self.playerid = playerid
        self.fieldID = fieldID
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.lessonID = lessonID
        self.coachID = coachID
        