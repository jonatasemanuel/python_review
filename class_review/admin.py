from user import User


class Admin(User):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges():
    def __init__(self) -> None:
        self.privileges = [
            'Can add post', 'Can delete post', 'Can ban user'
            ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'{privilege}')
    

boss = Admin('joey', 'santos')
boss.privileges.show_privileges()