
class MemberIn:
  # Track used IDs to avoid duplicates

    def __init__(
        self,
        name = None,
        surname = None,
        birthdate = None,
        phone = None,
        address = None,
        email = None,
        category = None,
        username = None,
        id = None
    ):
        
        self.id = id
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.phone = phone
        self.address = address
        self.email = email
        self.category = category
        self.username = username

