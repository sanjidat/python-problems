# Create a Bus object that will inherit all of the variables and methods of the Vehicle class and display it.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show(self):
        print('Vehicle Name: ', self.name, 'Speed: ', self.max_speed, 'Mileage: ', self.mileage) 

Bus = Vehicle("Volvo", 180, 12)
Bus.show()
