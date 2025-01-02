from __init__ import user_functions, member_functions
from entity_instances.member_in import MemberIn
from entity_instances.user_auth_in import UserAuthIn


class SignUp:
    def __init__(self, username):
        self.username = username
        


    def check_username(self):
        # placeholder for the actual username check logic
        if (self.username == "giorgis1"):
            print("!Username already exists. Please try again.!")
            return False
    
        return True

    def user_signup(self, password):
        # placeholder for the actual signup logic
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        birthdate = input("Enter your birthdate: ")
        phone = input("Enter your phone: ")
        address = input("Enter your address: ")
        email = input("Enter your email: ")
        category = input("Enter your category(player/coach): ")

        member = MemberIn(name, surname, birthdate, phone, address, email, category, self.username)
        member_functions.add_member(member)
        user = UserAuthIn(self.username, password)
        user_functions.add_user_auth(user)

        print(f"User {self.username} signed up successfully with password {password}.")