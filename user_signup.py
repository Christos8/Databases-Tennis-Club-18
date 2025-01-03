from __init__ import user_functions, member_functions, player_functions, coach_functions
from entity_instances.member_in import MemberIn
from entity_instances.user_auth_in import UserAuthIn
from entity_instances.player_in import PlayerIn
from entity_instances.coach_in import CoachIn



class SignUp:
    def __init__(self, username):
        self.username = username
        


    def check_username(self):
        # placeholder for the actual username check logic
        if (user_functions.check_username(self.username)):
            print("!Username already exists. Please try again.!")
            return False
    
        return True

    def user_signup(self, password):
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        birthdate = input("Enter your birthdate: ")
        phone = input("Enter your phone: ")
        address = input("Enter your address: ")
        email = input("Enter your email: ")
        category = input("Enter your category(player/coach): ")
        member = MemberIn(name, surname, birthdate, phone, address, email, category, self.username)
        member_functions.add_member(member)
        if category == "player":
            player = PlayerIn(self.username)
            player_functions.add_player(player)
        if category == "coach":
            coach = CoachIn(self.username)
            coach_functions.add_coach(coach)
        user = UserAuthIn(self.username, password)
        user_functions.add_user_auth(user)

        print(f"User {self.username} signed up successfully with password {password}.")