class PlayerIn:
    def __init__(self, MemberID=None):
        if not MemberID:
            raise ValueError("Player must be associated with a Member ID")
        
        self.MemberID = MemberID
