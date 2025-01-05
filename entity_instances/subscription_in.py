from datetime import date

class SubscriptionIn:
    def __init__(
        self,
        id	= None,
        startDate = None,
        endDate = None,
        type = None,
        category = None,
        status = None,
    ):
        self.id= id
        self.startDate = startDate
        self.endDate = endDate
        self.type = type
        self.category = category
        self.status = status #or self.set_status()


    # def set_status(self):
    #     today = date.today()
        
    #     if self.startDate and self.endDate:
    #         if self.startDate <= today <= self.endDate:
    #             return "Active"
    #         elif today > self.endDate:
    #             return "Upcoming"
    #         else:
    #             return "Check the Dates again"
    #     return "Set Dates"  
        
