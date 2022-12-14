class Restaurant():
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant's name: {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f'The {self.restaurant_name} is opening')

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f'Orders: {self.number_served}')

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(f'Ordered: {self.number_served}')


"""genius = Restaurant('Genius', 'Arab food')
genius.describe_restaurant()
genius.open_restaurant()

fastdog = Restaurant('Fastdog', 'Street food')
fastdog.describe_restaurant()
fastdog.open_restaurant()
"""
if __name__ == '__main__':
    sukiya = Restaurant('Sukiya', 'Japan food')
    # sukiya.describe_restaurant()
    # sukiya.open_restaurant()
    sukiya.set_number_served(12)
    sukiya.increment_number_served(20)
