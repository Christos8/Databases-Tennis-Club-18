from select_tables import SELECT_PROFILE, SELECT_RESERVATION
from update_tables import UPDATE_RESERVATION
from __init__ import member_functions

class PlayerMenu:

    def __init__(self, username):
        self.username = username
        self.player_options = ["Make a court reservation", "Participate in a lesson", "View profile", "logout", "Exit"]
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
                print("Make a court reservation")
                self.make_reservation()
            case 2:
                print("Participate in a lesson")
                self.participate_lesson()
            case 3:
                print("View profile")
                self.view_profile()
            case 4:
                print("Logging out...")
                self.logout()
            case 5:
                print("Exiting...")
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

    def make_reservation(self):
        # Implement the logic for making a court reservation
        pass

    def participate_lesson(self):
        # Implement the logic for participating in a lesson
        pass

    def view_profile(self):
        member = member_functions.return_member(self.username)
        if member:
            print(f"Profile details for user {member.username}:\n")
            print(f"Name: {member.name}")
            print(f"Surname: {member.surname}")
            print(f"Birthdate: {member.birthdate}")
            print(f"Phone: {member.phone}")
            print(f"Address: {member.address}")
            print(f"Email: {member.email}")
            print(f"Category: {member.category}")
            input("Press enter to return to main menu")
            PlayerMenu(self.username)
        else:
            print("Profile not found.")
    
    def logout(self):
        from login_menu import LoginMenu
        LoginMenu()