from entity_instances.equipment_rental_in import EquipmentRentalIn
from create_tables import CREATE_EQUIPMENT_RENTAL_TABLE
from insert_tables import INSERT_EQUIPMENT_RENTAL


class EquipmentRental:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_EQUIPMENT_RENTAL_TABLE)

    def add_equipment_rental(self, equipmentrent: EquipmentRentalIn):
        with self.connection:
            self.cursor.execute(INSERT_EQUIPMENT_RENTAL, (equipmentrent.playerID, equipmentrent.equipmentID, equipmentrent.rentDate))

    