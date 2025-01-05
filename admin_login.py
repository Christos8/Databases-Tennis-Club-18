from __init__ import tournament_functions, equipment_functions, field_functions, lesson_functions
from entity_instances.tournament_in import TournamentIn
from entity_instances.equipment_in import EquipmentIn
from entity_instances.field_in import FieldIn
from entity_instances.lesson_in import LessonIn


class AdminLogin:
    def __init__(self):
        pass


    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Create Tournament")
            print("2. Add Equipment")
            print("3. Add Court")
            print("4. Add Lesson")
            print("5. Logout")
            choice = int(input("Enter your choice: "))
            self.handle_choice(choice)

    def handle_choice(self, choice):
        match choice:
            case 1:
                self.create_tournament()
            case 2:
                self.add_equipment()
            case 3:
                self.add_field()
            case 4:
                self.add_lesson()
            case 5:
                print("Logging out...")
                exit()

    def create_tournament(self):
        deadline = input("Enter tournament deadline DD/MM/YYYY: ")
        fee = input("Enter tournament fee: ")
        prize = input("Enter tournament prize: ")
        date = input("Enter tournament date DD/MM/YYYY: ")
        sTime = input("Enter tournament start time: ")

        tournament = TournamentIn(
        id= None,
        deadline=deadline,
        fee=fee,
        prize=prize,
        date=date,
        sTime=sTime
        )
        # Add logic to create tournament
        tournament_functions.add_tournament(tournament)

    def add_equipment(self):
        description = input("Enter equipment description: ")
        characteristic_code = input("Enter equipment characteristic code: ")

        equipment = EquipmentIn(
        id = None,
        description = description,
        characteristicCode = characteristic_code,
        availability = 1
        )
        equipment_functions.add_equipment(equipment)
        print(f"Equipment '{description}' added successfully!")


    def add_field(self):
        type = input("Enter field type: ")
        field = FieldIn(
        id = None,
        type = type,
        status = 1
        )
        field_functions.add_field(field)

    def add_lesson(self):
        date = input("Enter lesson date DD/MM/YYYY: ")
        starttime = input("Enter lesson start time HH:MM: \n")
        endtime = input("Enter lesson end time HH:MM: \n")
        difficulty = input("Enter lesson difficulty (Begginers, Intermediates, Professionals): \n")
        fieldid = input("Enter the field the lesson is going to take place: \n1. Court 1: Grass\n2. Court 2: Hard\n3. Court 3: Clay\n4. Court 4: Hard\n")
        coachid = input("Enter the coach ID: \n")
        

        lesson = LessonIn(
        id= None,
        date= date,
        startTime= starttime,
        endTime= endtime,
        difficulty= difficulty,
        fieldid= fieldid,
        coachID= coachid

        )
        lesson_functions.add_lesson(lesson)
        print(f"Lesson added successfully!")