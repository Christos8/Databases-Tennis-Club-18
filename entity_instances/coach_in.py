class Coach_in:
    def __init__(self, memberID=None):
        if not memberID:
            raise ValueError("Coach must be associated with a member ID")
        
        self.memberID = memberID
