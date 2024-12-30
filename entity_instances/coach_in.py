class COACH_IN:
    def __init__(self, MemberID=None):
        if not MemberID:
            raise ValueError("Coach must be associated with a Member ID")
        
        self.MemberID = MemberID
