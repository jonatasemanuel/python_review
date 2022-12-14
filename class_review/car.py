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
        
        
if __name__ == '__main__':
    my_new_car = Car('ford', 'eco- sport', 2018)
    print(my_new_car.get_descriptive_name())
    print(my_new_car.update_odometer(90))
    my_new_car.increment_odometer(1302)
    print(f'This car has {my_new_car.odometer_reading} miles on it.')
