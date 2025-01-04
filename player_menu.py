from select_tables import SELECT_PROFILE, SELECT_RESERVATION
from update_tables import UPDATE_RESERVATION
from __init__ import member_functions, reservation_functions, lesson_functions
from entity_instances.reservation_in import ReservationIn

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