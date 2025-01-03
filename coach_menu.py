from select_tables import SELECT_LESSONS, SELECT_COACHID, SELECT_RESERVATION
from update_tables import UPDATE_RESERVATION

class CoachMenu:

    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.coach_options = ["Participate on a court reservation", "See your lessons", "Exit"]
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
                #self.login()
                print("Participate on a court reservation")
                self.reservation_part(UPDATE_RESERVATION, SELECT_COACHID, SELECT_RESERVATION)
            case 2:
                #self.login()
                print("See your lessons")
            case 3:
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

    
    def reservation_part(self, UPDATE_RESERVATION, SELECT_COACHID, SELECT_RESERVATION):
        name = input("Enter your username: ")
        self.cursor.execute(SELECT_COACHID, (name,))

        result = self.cursor.fetchone()

        if result:
            coachid = result[0]  
        else:
            print("Coach not found.")
            return
    
        Resid = input("Put the ID of the reservation you want to participate in: ")

        self.cursor.execute(SELECT_RESERVATION, (Resid,))
        reservation = self.cursor.fetchone()

        if reservation:
            self.cursor.execute(UPDATE_RESERVATION, (coachid, Resid))
            self.connection.commit()
            print(f"Coach {coachid} has been added to reservation {Resid}.")
        else:
            print(f"Reservation with ID {Resid} does not exist.")


    
    def lessons(self, SELECT_LESSONS):
        print("Your lessons are:")
        for lesson in SELECT_LESSONS:
            print(lesson)
        print("\n")
        #self.coach()
