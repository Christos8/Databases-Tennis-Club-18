from entity_instances.tournament_par_in import TournamentParIn
from create_tables import CREATE_TOURNAMENT_PARTICIPATION_TABLE
from insert_tables import INSERT_TOURNAMENT_PARTICIPATION
from select_tables import SELECT_TOURNAMENT_PARTICIPATION, SELECT_TOURNAMENT_PARTICIPATION_PLAYERID

class TournamentPar:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_TOURNAMENT_PARTICIPATION_TABLE)

    def add_tournament_par(self, tournamentpar: TournamentParIn):
        with self.connection:
            self.cursor.execute(INSERT_TOURNAMENT_PARTICIPATION, (tournamentpar.playerID, tournamentpar.tournamentID))

    def check_participation(self, tournamentpar: TournamentParIn):
        self.cursor.execute(SELECT_TOURNAMENT_PARTICIPATION , (tournamentpar.playerID, tournamentpar.tournamentID))
        return self.cursor.fetchone() is not None
    
    def get_user_tournaments(self, playerID):

        self.cursor.execute(SELECT_TOURNAMENT_PARTICIPATION_PLAYERID, (playerID,))
        return self.cursor.fetchall()