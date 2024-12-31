from entity_instances.equipment_in import EquipmentIn
from create_tables import CREATE_EQUIPMENT_TABLE
from insert_tables import INSERT_EQUIPMENT


class Equipment:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_EQUIPMENT_TABLE)

    def add_equipment(self, equipment: EquipmentIn):
        with self.connection:
            self.cursor.execute(INSERT_EQUIPMENT, (equipment.id, equipment.description, equipment.characteristicCode, equipment.availability))

    