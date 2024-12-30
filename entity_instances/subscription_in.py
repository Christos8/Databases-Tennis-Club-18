from datetime import date

class SUBSCRIPTION_IN:
    def __init__(
        self,
        ID	= None,
        StartDate = None,
        EndDate = None,
        Type = None,
        Category = None,
        Status = None,
    ):
        self.ID= ID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Type = Type
        self.Category = Category
        self.Status = Status or self.set_status()


    def set_status(self):
        today = date.today()
        
        if self.StartDate and self.EndDate:
            if self.StartDate <= today <= self.EndDate:
                return "Active"
            elif today > self.EndDate:
                return "Upcoming"
            else:
                return "Check the Dates again"
        return "Set Dates"  
        
