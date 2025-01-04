from select_tables import SELECT_PROFILE, SELECT_RESERVATION
from update_tables import UPDATE_RESERVATION
from __init__ import member_functions, tournament_functions, tournamentpar_functions
from entity_instances.tournament_par_in import TournamentParIn

class PlayerMenu:

    def __init__(self, username):
        self.member = member_functions.return_member(username)
        self.player_options = ["Participate in a tournament", "Make a court reservation", "Participate in a lesson", "View profile", "logout", "Exit"]
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
                print("Make a court reservation")
                self.make_reservation()
            case 3:
                print("Participate in a lesson")
                self.participate_lesson()
            case 4:
                print("View profile")
                self.view_profile()
            case 5:
                print("Logout")
                self.logout()
            case 6:
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
        print(tournament_par.playerID, tournament_par.tournamentID) 
        tournamentpar_functions.add_tournament_par(tournament_par)
        print("You have successfully registered for the tournament.")
      #  print(tournament_functions.display_tournament_participants())


    def make_reservation(self):
        # Implement the logic for making a court reservation
        pass

    def participate_lesson(self):
        # Implement the logic for participating in a lesson
        pass

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