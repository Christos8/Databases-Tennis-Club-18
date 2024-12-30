class SignUp:
    def __init__(self, username):
        self.username = username

    def check_username(self):
        # placeholder for the actual username check logic
        if (self.username == "giorgis"):
            print("!Username already exists. Please try again.!")
            return False
        return True

    def user_signup(self, password):
        # placeholder for the actual signup logic
        
        print(f"User {self.username} signed up successfully with password {password}.")