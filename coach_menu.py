from select_tables import SELECT_LESSONS, SELECT_COACHID, SELECT_RESERVATION
from update_tables import UPDATE_RESERVATION
from __init__ import coach_functions, lesson_functions

class CoachMenu:

    def __init__(self, username):
        self.username = username
        self.coach_options = ["Participate on a court reservation", "See your lessons", "logout", "Exit"]
        self.coach_display()
        coach_choice = self.get_coach_choice()
        self.handle_coach_choice(coach_choice)

    def coach_display(self):
        print("Choose what you wish to do!\n")
        for i, coach_option in enumerate(self.coach_options, 1):
            print(f"{i}. {coach_option}")
    
    
    def handle_coach_choice(self, user_choice):
        match user_choice:
            case 1:
                print("Participate on a court reservation")
                self.reservation_part()
            case 2:
                print("My lessons:\n")
                self.lessons()
            case 3:
                print("Logging out...")
                self.logout()
            case 4:
                print("Exiting...")
                exit()

    def get_coach_choice(self):
        while True:
            try:
                coach_choice = int(input("Enter your choice: "))
                if 1 <= coach_choice <= len(self.coach_options):
                    return coach_choice
                else:
                    print("Invalid choice. Please try again.")
                    CoachMenu()
            except ValueError:
                print("Invalid input. Please enter a number.")
                CoachMenu()

    
    def reservation_part(self):
        coach_functions.coach_reservation()


    
    def lessons(self):
        id = coach_functions.getid(self.username)
        lessons = lesson_functions.return_lesson(id)
        if lessons:
            for lesson in lessons:
                print(f"Lesson ID: {lesson.id}")
                print(f"Lesson Date: {lesson.date}")
                print(f"Starting Time: {lesson.startTime}")
                print(f"Ending Time: {lesson.endTime}")
                print(f"Difficulty: {lesson.difficulty}\n")
        else:
            print("Profile not found.")
            
        input("Press enter to return to main menu")
        CoachMenu(self.username)

   

    def logout(self):
        from login_menu import LoginMenu
        LoginMenu()