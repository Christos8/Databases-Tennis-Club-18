from entity_instances.tournament_par_in import TournamentParIn
from create_tables import CREATE_TOURNAMENT_PARTICIPATION_TABLE
from insert_tables import INSERT_TOURNAMENT_PARTICIPATION


class TournamentPar:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_TOURNAMENT_PARTICIPATION_TABLE)

    def add_tournament_par(self, tournamentpar: TournamentParIn):
        with self.connection:
            self.cursor.execute(INSERT_TOURNAMENT_PARTICIPATION, (tournamentpar.playerID, tournamentpar.tournamentID))

    