from user_login import UserLogin
from user_signup import SignUp
from coach_login import CoachLogin
from coach_menu import CoachMenu
from player_menu import PlayerMenu
from __init__ import player_functions, subscription_functions
from entity_instances.subscription_in import SubscriptionIn
from datetime import date, timedelta



class LoginMenu:
    def __init__(self):
        self.options = ["Player Login", "Coach Login", "Register", "Exit", "Admin"]
        self.display()
        choice = self.get_choice()
        self.handle_choice(choice)

    def display(self):
        print("\nWelcome to our tennis club! Please choose what you want to do:")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def user_display(self):
        print("Choose what you wish to do!\n")
        for i, player_option in enumerate(self.player_options, 1):
            print(f"{i}. {player_option}")


    def get_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
                    LoginMenu()
            except ValueError:
                print("Invalid input. Please enter a number.")
                LoginMenu()

    def handle_choice(self, choice):
        match choice:
            case 1:
                self.player_login()
            case 2:
                self.coach_login()
            case 3:
                self.register()
            case 4:
                print("Exiting...")
                exit()
            case 5:
                self.admin_menu()

    def player_login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_login = UserLogin(username, password)
        if user_login.login():
            print("\nWelcome to the tennis club!")
            player_id = player_functions.get_player_id(username)
            if subscription_functions.check_subscription(player_id):
                print("You have an active subscription.")
                PlayerMenu(username)
            else:
                print("You do not have an active subscription.")
                input("Press Enter to subscribe.")   
                startdate = date.today().strftime("%d/%m/%Y")
                type1 = input("Enter the type of subscription: \n1. Monthly\n2. 6 months\n3. Yearly\n")
                if type1 == "1":
                    type = "Monthly"
                    end = date.today() + timedelta(days=30)
                    enddate = end.strftime("%d/%m/%Y")
                elif type1 == "2":
                    type = "6 months"
                    end = date.today() + timedelta(days=180)
                    enddate = end.strftime("%d/%m/%Y")
                elif type1 == "3": 
                    type = "Yearly"
                    end = date.today() + timedelta(days=365)
                    enddate = end.strftime("%d/%m/%Y")
                input("Press Enter to confirm subscription.")
                print(enddate)
                status = "Active"
                print(status)
                category = "player"
                print(category)
                sub = SubscriptionIn(startdate, enddate, type, category, status, player_id)   
                subscription_functions.add_subscription(sub)
                print("You have successfully subscribed.")
                PlayerMenu(username) 
        else:
            print("Invalid username or password. Please try again.")
            LoginMenu()


    def coach_login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        coach_login = CoachLogin(username, password)
        if coach_login.login():
            print("\nWelcome to the tennis club!")
            CoachMenu(username)
        else:
            print("Invalid username or password. Please try again.")
            LoginMenu()


    
    def register(self):
        username = input("Enter your username: ")
        user_signup = SignUp(username)
        if user_signup.check_username():
            password = input("Enter your password: ")
            user_signup.user_signup(password)
        self.display()
        choice = self.get_choice()
        self.handle_choice(choice)

    
    def get_user_choice(self):
        while True:
            try:
                user_choice = int(input("Enter your choice: "))
                if 1 <= user_choice <= len(self.player_options):
                    return user_choice
                else:
                    print("Invalid choice. Please try again.")
                    LoginMenu()
            except ValueError:
                print("Invalid input. Please enter a number.")
                LoginMenu()

    def handle_player_choice(self, user_choice):
        match user_choice:
            case 1:
                #self.login()
                print("Make a reservation")
            case 2:
                #self.login()
                print("Take part on a lesson")
            case 3:
                print("Exiting...")
                exit()

    def admin_menu(self):
        from admin_login import AdminLogin
        admin_login = AdminLogin()
        admin_login.admin_menu()