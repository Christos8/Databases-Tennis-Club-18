from datetime import date
from select_tables import SELECT_PROFILE, SELECT_RESERVATION
from update_tables import UPDATE_RESERVATION
from __init__ import member_functions,equipment_functions,equipment_rental_functions, reservation_functions, lesson_functions, lessonpar_functions, tournament_functions, tournamentpar_functions, player_functions
from entity_instances.reservation_in import ReservationIn
from entity_instances.tournament_par_in import TournamentParIn
from entity_instances.equipment_rental_in import EquipmentRentalIn
from entity_instances.lesson_par_in import LessonParticipationIn

class PlayerMenu:

    def __init__(self, username):
        self.member = member_functions.return_member(username)
        self.player_options = ["Participate in a tournament","Show my tournaments" ,
        "Rent equipment","Show my rentals", "Return equipment",
        "Make a court reservation", "Participate in a lesson", "View profile", "logout", "Exit"]
        self.player_display()
        player_choice = self.get_player_choice()
        self.handle_player_choice(player_choice)

    def player_display(self):
        print("\nChoose what you wish to do!\n")
        for i, player_option in enumerate(self.player_options, 1):
            print(f"{i}. {player_option}")

    def handle_player_choice(self, player_choice):
        match player_choice:
            case 1:
                print("Participate in a tournament\n")
                self.participate_tournament()
                PlayerMenu(self.member.username)
            case 2:
                print("Show my tournaments\n")
                self.show_my_tournaments()
                input("Press enter to return to main menu")
                PlayerMenu(self.member.username)
            case 3:
                print("Rent equipment\n")
                self.rent_equipment()
                input("Press enter to return to main menu")
                PlayerMenu(self.member.username)
            case 4:
                print("Show my rentals\n")
                self.show_my_rentals()
                input("Press enter to return to main menu")
                PlayerMenu(self.member.username)
            case 5:
                print("Return equipment\n")
                self.return_equipment()
                input("Press enter to return to main menu")
                PlayerMenu(self.member.username)
            case 6:
                print("Make a court reservation\n")
                self.make_reservation()
                PlayerMenu(self.member.username)
            case 7:
                print("Participate in a lesson\n")
                self.participate_lesson()
                PlayerMenu(self.member.username)
            case 8:
                print("View profile\n")
                self.view_profile()
                input("Press enter to return to main menu")
                PlayerMenu(self.member.username)                
            case 9:
                print("Logout\n")
                self.logout()
            case 10:
                print("Exiting...\n")
                exit()
            case _:
                print("Invalid choice. Please try again.")
                PlayerMenu(self.member.username)

    def get_player_choice(self):
        while True:
            try:
                player_choice = int(input("Enter your choice: "))
                if 1 <= player_choice <= len(self.player_options):
                    return player_choice
                else:
                    print("Invalid choice. Please try again.")
                    PlayerMenu(self.member.username)
            except ValueError:
                print("Invalid input. Please enter a number.")
                PlayerMenu(self.member.username)

    def participate_tournament(self):
        # Implement the logic for participating in a tournament
        tournament_functions.display_tournaments()
        try:
            tournament_id = int(input("Enter the ID of the tournament you wish to participate in: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            PlayerMenu(self.member.username)
        tournament_par = TournamentParIn(self.member.id, tournament_id)
        if tournamentpar_functions.check_participation(tournament_par):
            print("You have already registered for this tournament.")
        else:
            tournamentpar_functions.add_tournament_par(tournament_par)
            print("You have successfully registered for the tournament.")

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

    def rent_equipment(self):
        equipment_functions.display_equipment()
        equipment_id = int(input("Enter the ID of the equipment you wish to rent: "))
        equipment = equipment_functions.return_equipment_from_id(equipment_id)
        current_date = date.today()

        if equipment:
            if equipment.availability:
                rental = EquipmentRentalIn(self.member.id, equipment_id, current_date)
                equipment_rental_functions.add_equipment_rental(rental)
                equipment_functions.update_equipment_availability(equipment_id, 0)
                print("Equipment rented successfully.")
            else:
                print("Equipment is not available.")
        else:
            print("Equipment not found.")

    def show_my_rentals(self):
        my_rentals = equipment_rental_functions.get_user_rentals(self.member.id)

        if my_rentals:
            print("Equipment you have rented:")
            for i in my_rentals:
                equipment = equipment_functions.return_equipment_from_id(i.equipmentID)
                print(f"""ID: {equipment.id}\nDescription: {equipment.description}\nCharacteristic Code: {equipment.characteristicCode}\nRent Date: {i.rentDate}\n""")
            return True
        else:
            print("You have not rented any equipment.")
            return False
        

    def return_equipment(self):
        if self.show_my_rentals():
            equipment_id = int(input("Enter the ID of the equipment you wish to return: "))
            equipment_functions.update_equipment_availability(equipment_id, 1)
            equipment_rental_functions.delete_equipment_rental(self.member.id, equipment_id)
            print("Equipment returned successfully!\n")

    def make_reservation(self):
        fieldid = input("Enter the number of the court you would like to book: \n1. Court 1: Grass\n2. Court 2: Clay\n3. Court 3: Hard\n4. Court 4: Hard\n")
        date = input("Enter the date of the reservation: DD/MM/YYYY\n")
        starttime = input("Enter the starting time: HH:MM\n")
        endtime = input("Enter the ending time: HH:MM\n")
        playerid = player_functions.get_player_id(self.member.username)
        lessonid = None
        coachid = None

        if (reservation_functions.check_reservation_exists(fieldid, date, starttime, endtime)):
            input("This field is already reserved on this date and time. Press enter to make the reservation again.")
            self.make_reservation()    
        else:     
            reservation = ReservationIn(playerid=playerid, fieldID=fieldid, date=date, startTime=starttime, endTime=endtime, lessonID=lessonid, coachID=coachid)
            reservation_functions.add_reservation(reservation)
            print("Reservation made successfully.\n")
            input("Press enter to return to main menu")
        

    def participate_lesson(self):
        # Implement the logic for participating in a lesson
        lesson_functions.display_lessons()
        lesson_id = int(input("Enter the ID of the lesson you wish to participate in: "))
        lesson_par = LessonParticipationIn(self.member.id, lesson_id)
        if lessonpar_functions.check_participation(lesson_par):
            print("You have already registered for this lesson.")
        else:
            lessonpar_functions.add_lesson_par(lesson_par)
            print("You have successfully registered for the lesson.")
        


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
        else:
            print("Profile not found.")
    
    def logout(self):
        from login_menu import LoginMenu
        LoginMenu()