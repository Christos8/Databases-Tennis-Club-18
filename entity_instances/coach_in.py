class CoachIn:
    def __init__(self, memberID=None):
        if not memberID:
            raise ValueError("Coach must be associated with a Member ID")
        
        self.memberID = memberID
