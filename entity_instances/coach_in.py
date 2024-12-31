#current file is /entity_instances/coach_in.py there are
# 15 similar py files in the same directory please change them all to
# use CamelCase for class Names 
class Coachin:
    def __init__(self, MemberID=None):
        if not MemberID:
            raise ValueError("Coach must be associated with a Member ID")
        
        self.MemberID = MemberID
