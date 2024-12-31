from datetime import timedelta
import random

class MemberIn:

    existing_ids = set()  # Track used IDs to avoid duplicates

    def __init__(
        self,
        id = None,
        name = None,
        surname = None,
        birthdate = None,
        phone = None,
        address = None,
        email = None,
        category = None,
        username = None,
    ):
        
         # Generate unique ID
        while not id or id in MemberIn.existing_ids:
            id = random.randint(1, 1000)
        
        MemberIn.existing_ids.add(id)

        self.id = id
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.phone = phone
        self.address = address
        self.email = email
        self.category = category
        self.username = username

