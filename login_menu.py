from user_login import UserLogin
from user_signup import SignUp

class LoginMenu:
    def __init__(self):
        self.options = ["Player Login", "Coach Login", "Register", "Exit"]
        self.display()
        choice = self.get_choice()
        self.handle_choice(choice)

    def display(self):
        print("Welcome to our tennis club! Please choose what you want to do:")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def handle_choice(self, choice):
        match choice:
            case 1:
                self.login()
            case 2:
                self.login()
            case 3:
                self.register()
            case 4:
                print("Exiting...")
                exit()

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_login = UserLogin(username, password)
        if user_login.login():
            print("Welcome to the tennis club!")
        else:
            print("Invalid username or password. Please try again.")
    
    def register(self):
        username = input("Enter your username: ")
        user_signup = SignUp(username)
        if user_signup.check_username():
            password = input("Enter your password: ")
            user_signup.user_signup(password)
        self.display()
        choice = self.get_choice()
        self.handle_choice(choice)