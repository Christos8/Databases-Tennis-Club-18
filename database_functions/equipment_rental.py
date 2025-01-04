from entity_instances.equipment_rental_in import EquipmentRentalIn
from create_tables import CREATE_EQUIPMENT_RENTAL_TABLE
from insert_tables import INSERT_EQUIPMENT_RENTAL
from select_tables import SELECT_EQUIPMENT_RENTAL_FROM_PLAYERID
from delete_tables import DELETE_EQUIPMENT_RENTAL

class EquipmentRental:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_EQUIPMENT_RENTAL_TABLE)

    def add_equipment_rental(self, equipmentrent: EquipmentRentalIn):
        with self.connection:
            self.cursor.execute(INSERT_EQUIPMENT_RENTAL, (equipmentrent.playerID, equipmentrent.equipmentID, equipmentrent.rentDate))

    def get_user_rentals(self, playerID):
        self.cursor.execute(SELECT_EQUIPMENT_RENTAL_FROM_PLAYERID, (playerID,))
        rentals = []
        for rental in self.cursor.fetchall():
            rentals.append(EquipmentRentalIn(rental[0], rental[1], rental[2]))
        
        return rentals
    
    def delete_equipment_rental(self, playerID, equipmentID):
        with self.connection:
            self.cursor.execute(DELETE_EQUIPMENT_RENTAL, (playerID, equipmentID))