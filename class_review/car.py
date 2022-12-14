class Car():
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 3988

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        return self.odometer_reading

    def increment_odometer(self, mileage):
        if mileage > 0:
            self.odometer_reading += mileage
        else:
            print("You can't roll back an odometer!")


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
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


if __name__ == '__main__':
    my_new_car = Car('ford', 'eco- sport', 2018)
    print(my_new_car.get_descriptive_name())
    print(my_new_car.update_odometer(90))
    my_new_car.increment_odometer(1302)
    print(f'This car has {my_new_car.odometer_reading} miles on it.')
