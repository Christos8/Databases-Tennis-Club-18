from entity_instances.tournament_in import TournamentIn
from create_tables import CREATE_TOURNAMENT_TABLE
from insert_tables import INSERT_TOURNAMENT
from select_tables import SELECT_TOURNAMENTS_ALL, SELECT_TOURNAMENT_FROM_ID


class Tournament:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_TOURNAMENT_TABLE)

    def add_tournament(self, tournament: TournamentIn):
        with self.connection:
            self.cursor.execute(INSERT_TOURNAMENT, (tournament.deadline, tournament.fee, tournament.prize, tournament.date, tournament.sTime))

    def display_tournaments(self):

        self.cursor.execute(SELECT_TOURNAMENTS_ALL)
        tournaments = self.cursor.fetchall()
        for tournament in tournaments:
            print(f"""
                  Tournament ID: {tournament[0]}
                  Deadline: {tournament[1]}
                  Fee: {tournament[2]}
                  Prize: {tournament[3]}
                  Date: {tournament[4]}
                  Start Time: {tournament[5]}
                  """)   
            
    def show_tournament_participants(self, tournament_id):
        self.cursor.execute(SELECT_TOURNAMENTS_ALL, (tournament_id,))
        participants = self.cursor.fetchall()
        for participant in participants:
            print(f"""
                  Player ID: {participant[0]}
                  Tournament ID: {participant[1]}
                  """)
    
    def return_tournament_from_id(self, tournament_id):
        self.cursor.execute(SELECT_TOURNAMENT_FROM_ID, (tournament_id,))
        tournament = TournamentIn(*self.cursor.fetchone())
        return tournament