from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")


class EquipmentIn:
    def __init__(
        self,
        ID = None,
        Description = None,
        CharacteristicCode = None,
        Availability = None,
    ):
        self.ID = ID
        self.Description = Description
        self.CharacteristicCode = CharacteristicCode
        self.Availability = ( Availability
                             or fake.random_choices(
                                 elements=[
                                     "Available",
                                     "Taken",
                                 ],
                                 length = 1,
                             ).pop()
        )
        

