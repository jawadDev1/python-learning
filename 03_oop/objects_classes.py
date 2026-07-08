from pydantic import BaseModel


class Human:
    def __init__(self, name, occupation) -> None:
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "pirate":
            print(self.name, "find the one piece.")

        elif self.occupation == "actor":
            print(self.name, "shoots a film.")

    def speaks(self):
        print(self.name, "says how are you?")


tom_cruise = Human("Tom Cruise", "actor")
luffy = Human("Monkey D. Luffy", "pirate")

# tom_cruise.do_work()
# tom_cruise.speaks()


# luffy.do_work()
# luffy.speaks()


# Inheritence
class Vehical:
    def general_usage(self):
        print("general use: Transportation")


class Car(Vehical):
    def __init__(self) -> None:
        print("i am car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vaccation with family")


class MotorBike(Vehical):
    def __init__(self) -> None:
        print("i am motorbike")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("specific use: ride in mountains, road trip")


c = Car()
c.general_usage()
c.specific_usage()


b = MotorBike()
b.general_usage()
b.specific_usage()

print(isinstance(c, Car))
print(issubclass(Car, Vehical))


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        return self.salary * 0.10


emp1 = Employee("Luffy", 50000)

emp1.name
print(emp1.calc_bonus())


# Enforces type safety
class Recipe(BaseModel):
    title: str
    calories: int


dal = Recipe(title="Moong Daal", calories=2888)
