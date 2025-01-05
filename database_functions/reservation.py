from entity_instances.reservation_in import ReservationIn
from create_tables import CREATE_RESERVATION_TABLE
from insert_tables import INSERT_RESERVATION


class Reservation:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_RESERVATION_TABLE)

    def add_reservation(self, reservation: ReservationIn):
        with self.connection:
            self.cursor.execute(INSERT_RESERVATION, (reservation.playerid, reservation.fieldID, reservation.date, reservation.startTime, reservation.endTime, reservation.lessonID, reservation.coachID))

    