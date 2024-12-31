from faker import Faker

Faker.seed(1234)
fake = Faker(locale="el_GR")


class EquipmentIn:
    def __init__(
        self,
        id = None,
        description = None,
        characteristicCode = None,
        availability = None,
    ):
        self.id = id
        self.description = description
        self.characteristicCode = characteristicCode
        self.availability = ( availability
                             or fake.random_choices(
                                 elements=[
                                     "Available",
                                     "Taken",
                                 ],
                                 length = 1,
                             ).pop()
        )
        

