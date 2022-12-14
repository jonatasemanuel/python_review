class User():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        return full_name

    def greet_user(self):
        print(f"Hello {self.describe_user()}, nice too met you")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Login attempts: {self.login_attempts}')

    def reset_loggin_attempts(self):
        self.login_attempts = 0
        print(f'Login attempts: {self.login_attempts}')


joe = User('joe', 'silva')
joe.greet_user()
joe.increment_login_attempts()
joe.increment_login_attempts()
joe.increment_login_attempts()
joe.reset_loggin_attempts()
