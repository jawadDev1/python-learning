from pydantic import BaseModel


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
