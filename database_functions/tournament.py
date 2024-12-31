from entity_instances.tournament_in import TournamentIn
from create_tables import CREATE_TOURNAMENT_TABLE
from insert_tables import INSERT_TOURNAMENT


class Tournament:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_TOURNAMENT_TABLE)

    def add_tournament(self, tournament: TournamentIn):
        with self.connection:
            self.cursor.execute(INSERT_TOURNAMENT, (tournament.id, tournament.deadline, tournament.fee, tournament.prize, tournament.date, tournament.sTime))

    