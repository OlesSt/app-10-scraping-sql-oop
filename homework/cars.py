class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descript(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name

    def read_odometer(self):
        print(f"Run: {self.odometer_reading}")

    def update_odometer(self, miles):
        self.odometer_reading = miles
        return miles

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_tanf(self, litr):
        print(f"Tank full of {litr} liters")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def fill_tanf(self, litr):
        print("NO")


# __MAIN__
new_car = Car("audi", "q6", 2012)
print(new_car.get_descript())

old_car = Car("bmw", "x3", 2007)
old_car.update_odometer(34200)
print(old_car.get_descript())
old_car.read_odometer()
old_car.increment_odometer(4000)
old_car.read_odometer()

elec_car = ElectricCar("tesla", "model x", 2020)
print(elec_car.get_descript())

old_car.fill_tanf(20)
elec_car.fill_tanf(20)