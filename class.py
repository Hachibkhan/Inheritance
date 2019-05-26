class Vehicle:

    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):

        self.name = name

        self.manufacturer = manufacturer

        self.color = color


    def drive(self):

        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):

        print("Turning", self.name, "to", direction)

    def brake(self):

        print(self.name, "is stopping!")


class Car(Vehicle):

    def __init__(self, name, manufacturer, color, year):
        
        print("Creating a car")

        super().__init__(name, manufacturer, color)

        self.year = 2016

        self.wheels = 4

    def change_gear(self, gear_name):

        print(self.name, "is changing gear to", gear_name)

    def turn(self, direction):

        print(self.name, "is turning", direction)

if __name__ == "__main__":

    c = Car("Hero Honda", "Walton", "Red", 2016)

    print(c.name, c.year, c.wheels)




    



