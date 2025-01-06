from entity_instances.reservation_in import ReservationIn
from create_tables import CREATE_RESERVATION_TABLE
from insert_tables import INSERT_RESERVATION
from select_tables import SELECT_RESERVATION_EXISTS, SELECT_RESERVATIONS_BY_MONTH


class Reservation:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_RESERVATION_TABLE)

    def add_reservation(self, reservation: ReservationIn):
        with self.connection:
            self.cursor.execute(INSERT_RESERVATION, (reservation.playerid, reservation.fieldID, reservation.date, reservation.startTime, reservation.endTime, reservation.lessonID, reservation.coachID))

    def check_reservation_exists(self, fieldID, date, startTime, endTime):
        self.cursor.execute(SELECT_RESERVATION_EXISTS, (fieldID, date, startTime, endTime))
        return self.cursor.fetchone() is not None
    
    def get_reservations_by_month(self, month):
        self.cursor.execute(SELECT_RESERVATIONS_BY_MONTH, (month,))
        reservations = []
        for reservation in self.cursor.fetchall():
            reservations.append(ReservationIn(reservation[0] ,reservation[1], reservation[2], reservation[3], reservation[4], reservation[5], reservation[6], reservation[7]))
        return reservations