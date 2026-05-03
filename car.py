class Car:
    def __init__(self, car_id, brand, year, color, milage=0.0):
        self.car_id = car_id
        self.brand = brand
        self.year = year
        self.color = color
        self.milage = milage

    def change_color(self, new_color):
        self.color = new_color

    def drive(self, miles):
        self.milage += miles 

    def __str__(self):
        return f"{self.car_id} - {self.year} {self.color} {self.brand} with {self.milage} miles"
        



