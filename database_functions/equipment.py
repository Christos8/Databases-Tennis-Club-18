from entity_instances.equipment_in import EquipmentIn
from create_tables import CREATE_EQUIPMENT_TABLE
from insert_tables import INSERT_EQUIPMENT
from select_tables import SELECT_ALL_EQUIPMENT, SELECT_EQUIPMENT_FROM_ID
from update_tables import UPDATE_EQUIPMENT_STATUS


class Equipment:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_EQUIPMENT_TABLE)

    def add_equipment(self, equipment: EquipmentIn):
        with self.connection:
            self.cursor.execute(INSERT_EQUIPMENT, (equipment.id, equipment.description, equipment.characteristicCode, equipment.availability))

    def return_equipment_from_id(self, equipment_id):
        self.cursor.execute(SELECT_EQUIPMENT_FROM_ID, (equipment_id,))
        equipment = EquipmentIn(*self.cursor.fetchone())
        return equipment

    def update_equipment_availability(self, equipment_id, availability):
        with self.connection:
            self.cursor.execute(UPDATE_EQUIPMENT_STATUS, (availability, equipment_id))

    def display_equipment(self):
        self.cursor.execute(SELECT_ALL_EQUIPMENT)
        equipment = self.cursor.fetchall()
        for equipment in equipment:
            availability_status = "Available" if equipment[3] != 0 else "Not Available"
            print(f""" 
            ID: {equipment[0]}
            Description: {equipment[1]}
            Characteristic Code: {equipment[2]}
            Availability: {availability_status}
            """)