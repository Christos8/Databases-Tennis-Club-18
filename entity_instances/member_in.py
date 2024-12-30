from datetime import timedelta
import random

class MEMBER_IN:

    existing_ids = set()  # Track used IDs to avoid duplicates

    def __init__(
        self,
        ID = None,
        Name = None,
        Surname = None,
        Birthdate = None,
        Phone = None,
        Address = None,
        Email = None,
        Category = None,
        Username = None,
    ):
        
         # Generate unique ID
        while not ID or ID in MEMBER_IN.existing_ids:
            ID = random.randint(1, 1000)
        
        MEMBER_IN.existing_ids.add(ID)

        self.ID = ID
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Phone = Phone
        self.Address = Address
        self.Email = Email
        self.Category = Category
        self.Username = Username

