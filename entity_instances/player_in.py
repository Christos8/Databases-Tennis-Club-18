class PlayerIn:
    def __init__(self, memberID=None):
        if not memberID:
            raise ValueError("Player must be associated with a member ID")
        
        self.memberID = memberID
