from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    def __init__(self, battery_size=70) -> None:
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'This car has a {self.battery_size} -kWh battery.')

    def get_range(self):
        if self.battery_size == 70: range = 240
        elif self.battery_size == 85: range = 270
        message = f'This car go approximately {range} miles on a full charge.'
        print(message)


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name()) 
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
