from random import randint


class Die():
    def __init__(self, sides) -> None:
        self.sides = sides
    
    def roll_die(self):
        rolling = randint(1, self.sides)
        print(f'Roll d{self.sides}: {rolling}')
    


six = Die(6)
six.roll_die()

ten = Die(10)
ten.roll_die()

twenty = Die(20)
twenty.roll_die()