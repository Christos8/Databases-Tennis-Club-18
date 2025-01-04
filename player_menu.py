from select_tables import SELECT_PROFILE, SELECT_RESERVATION
from update_tables import UPDATE_RESERVATION
from __init__ import member_functions, reservation_functions, lesson_functions,tournament_functions, tournamentpar_functions
from entity_instances.reservation_in import ReservationIn
from entity_instances.tournament_par_in import TournamentParIn

class PlayerMenu:

    def __init__(self, username):
        self.member = member_functions.return_member(username)
        self.player_options = ["Participate in a tournament","Show my tournaments" , "Make a court reservation", "Participate in a lesson", "View profile", "logout", "Exit"]
        self.player_display()
        player_choice = self.get_player_choice()
        self.handle_player_choice(player_choice)

    def player_display(self):
        print("Choose what you wish to do!\n")
        for i, player_option in enumerate(self.player_options, 1):
            print(f"{i}. {player_option}")

    def handle_player_choice(self, player_choice):
        match player_choice:
            case 1:
                print("Participate in a tournament")
                self.participate_tournament()
            case 2:
                print("Show my tournaments")
                self.show_my_tournaments()
            case 3:
                print("Make a court reservation")
                self.make_reservation()
            case 4:
                print("Participate in a lesson")
                self.participate_lesson()
            case 5:
                print("View profile")
                self.view_profile()
            case 6:
                print("Logout")
                self.logout()
            case 7:
                print("Exit")
                exit()

    def get_player_choice(self):
        while True:
            try:
                player_choice = int(input("Enter your choice: "))
                if 1 <= player_choice <= len(self.player_options):
                    return player_choice
                else:
                    print("Invalid choice. Please try again.")
                    PlayerMenu(self.username)
            except ValueError:
                print("Invalid input. Please enter a number.")
                PlayerMenu(self.username)

    def participate_tournament(self):
        # Implement the logic for participating in a tournament
        tournament_functions.display_tournaments()
        tournament_id = int(input("Enter the ID of the tournament you wish to participate in: "))
        tournament_par = TournamentParIn(self.member.id, tournament_id)
        if tournamentpar_functions.check_participation(tournament_par):
            print("You have already registered for this tournament.")
        else:
            tournamentpar_functions.add_tournament_par(tournament_par)
            print("You have successfully registered for the tournament.")
        PlayerMenu(self.member.username)

    def show_my_tournaments(self):
        # Implement the logic for showing the tournaments that the player has registered for
        my_tournaments = tournamentpar_functions.get_user_tournaments(self.member.id)
        if my_tournaments:
            print("Tournaments you have registered for:")
            for i in my_tournaments:
                tournament = tournament_functions.return_tournament_from_id(i[0])
                print(f"Deadline: {tournament.deadline}\nFee: {tournament.fee}\nPrize: {tournament.prize}\nDate: {tournament.date}\nStart Time: {tournament.sTime}\n")
        else:
            print("You have not registered for any tournaments.")
        input("Press enter to return to main menu")
        PlayerMenu(self.member.username)

    def make_reservation(self):
        fieldid = input("Enter the number of the court you would like to book: \n1. Court 1: Grass\n2. Court 2: Clay\n3. Court 3: Hard\n4. Court 4: Hard")
        starttime = input("Enter the starting time: ")
        endtime = input("Enter the ending time: ")
        lessonid = None
        coachid = None

        reservation = ReservationIn(fieldid, starttime, endtime, lessonid, coachid)
        reservation_functions.add_reservation(reservation)

        print("Reservation made successfully.")
        

    def participate_lesson(self):
        # Implement the logic for participating in a lesson

        lesson = lesson_functions.return_lesson()
        if lesson:
            print("Lessons available:")
            for i in lesson:
                print(f"Lesson no.{i.id}. At {i.date}, startin at {i.starttime} and ending at {i.endtime} with difficulty {i.difficulty} and with the coach {i.coachid}")

    def view_profile(self):
        if self.member:
            print(f"Profile details for user {self.member.username}:\n")
            print(f"Name: {self.member.name}")
            print(f"Surname: {self.member.surname}")
            print(f"Birthdate: {self.member.birthdate}")
            print(f"Phone: {self.member.phone}")
            print(f"Address: {self.member.address}")
            print(f"Email: {self.member.email}")
            print(f"Category: {self.member.category}")
            input("Press enter to return to main menu")
            PlayerMenu(self.member.username)
        else:
            print("Profile not found.")
    
    def logout(self):
        from login_menu import LoginMenu
        LoginMenu()