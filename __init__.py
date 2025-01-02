import sqlite3

from database_functions.member import Member
from database_functions.player import Player
from database_functions.coach import Coach
from database_functions.player_sub import PlayerSub
from database_functions.subscription import Subscription
from database_functions.equipment_rental import EquipmentRental
from database_functions.equipment import Equipment
from database_functions.tournament_par import TournamentPar
from database_functions.tournament import Tournament
from database_functions.lesson_par import LessonPar
from database_functions.lesson import Lesson 
from database_functions.player_res import PlayerRes
from database_functions.reservation import Reservation
from database_functions.field_res import FieldRes
from database_functions.field import Field
from database_functions.user_auth import UserAuth


connection = sqlite3.connect("./tennis-club.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

member_functions = Member(cursor, connection)
player_functions = Player(cursor, connection)
coach_functions = Coach(cursor, connection)
playersub_functions = PlayerSub(cursor, connection)
subscription_functions = Subscription(cursor, connection)
equipment_rental_functions = EquipmentRental(cursor, connection)
equipment_functions = Equipment(cursor, connection)
tournamentpar_functions = TournamentPar(cursor, connection)
tournament_functions = Tournament(cursor, connection)
lessonpar_functions = LessonPar(cursor, connection)
lesson_functions = Lesson(cursor, connection)
playerres_functions = PlayerRes(cursor, connection)
reservation_functions = Reservation(cursor, connection)
fieldres_functions = FieldRes(cursor, connection)
field_functions = Field(cursor, connection)
user_functions = UserAuth(cursor, connection)