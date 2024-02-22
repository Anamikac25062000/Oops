# 8)show class method, static method and instance method with simple example.

class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour
        Vehicle.total_vehicles += 1

    # Instance Method
    def display_details(self):
        print(f"{self.brand} of {self.model} model - Colour: {self.colour}")

    # Class Method
    @classmethod
    def all_vehicles(cls):
        return cls.total_vehicles

    # Static Method
    @staticmethod
    def is_colour(colour):
        colour_types = ['Red', 'Black', 'Blue']
        return colour in colour_types

car1 = Vehicle("Tesla", "Semi", "Black")
car2 = Vehicle("Honda", "Civic", "Red")
car3 = Vehicle("Toyota", "Camry", "Blue")

car1.display_details()

total_vehicles = Vehicle.all_vehicles()
print(f"Total Vehicles: {total_vehicles}")

colour = "Awesome"
appearance = Vehicle.is_colour(colour)
print(f"Is {colour} and very nice {appearance}")
