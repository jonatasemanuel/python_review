class Dog():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name.title()} is now sitting')
    
    def roll_over(self):
        print(f'{self.name.title()} rolled over!')


jake = Dog('jake', 28)
jake.sit()
jake.roll_over()
