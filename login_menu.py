from user_login import UserLogin
from user_signup import SignUp
from coach_login import CoachLogin
from coach_menu import CoachMenu

class LoginMenu:
    def __init__(self):
        self.options = ["Player Login", "Coach Login", "Register", "Exit"]
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

    def player_login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_login = UserLogin(username, password)
        if user_login.login():
            print("\nWelcome to the tennis club!")
            
            self.player_options = ["Make a court reservation", "Participate on a tennis lesson", "Exit"]
            self.user_display()
            user_choice = self.get_user_choice()
            self.handle_player_choice(user_choice)
        else:
            print("Invalid username or password. Please try again.")
            LoginMenu()


    def coach_login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        coach_login = CoachLogin(username, password)
        if coach_login.login():
            print("\nWelcome to the tennis club!")
            CoachMenu(username, password)
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

