from entity_instances.field_reserv_in import FieldReservationIn
from create_tables import CREATE_FIELD_RESERVATION_TABLE
from insert_tables import INSERT_FIELD_RESERVATION


class Field:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_FIELD_RESERVATION_TABLE)

    def add_field_reservation(self, fieldres: FieldReservationIn):
        with self.connection:
            self.cursor.execute(INSERT_FIELD_RESERVATION, (fieldres.reservationID, fieldres.reservationID))

    