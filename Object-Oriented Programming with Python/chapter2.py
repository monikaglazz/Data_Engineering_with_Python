# import datetime from datetime
from datetime import datetime
# Import pandas as pd
import pandas as pd


# ex 1
class Player:
    MAX_POSITION = 10
    MAX_SPEED = 3

    def __init__(self):
        self.position = 0

    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position = self.position + steps
        else:
            self.position = Player.MAX_POSITION

    def draw(self):
        drawing = "-" * self.position + "|" + "-" * \
            (Player.MAX_POSITION - self.position)
        print(drawing)


p = Player()
p.draw()
p.move(4)
p.draw()
p.move(5)
p.draw()
p.move(3)
p.draw()


# ex 2
# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")

# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")

# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")

# Print Player.MAX_SPEED
print(Player.MAX_SPEED)


# ex 3
class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    @classmethod
    def from_datetime(cls, datetime):
        year, month, day = datetime.year, datetime.month, datetime.day
        return cls(year, month, day)


b = BetterDate.from_str('2020-04-30')
print(b.year)
print(b.month)
print(b.day)

today = datetime.today()
bd = BetterDate.from_datetime(today)
print(bd.year)
print(bd.month)
print(bd.day)


# ex 4
class Employee:
    MIN_SALARY = 30000

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):

    def display(self):
        print("Manager", self.name)

    # added at ex 5
    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # added at ex 5
    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        Employee.give_raise(self, amount*bonus)


mng = Manager("Debbie Lashko", 86500)
print(mng.name)

mng.display()


# ex 5
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)


# ex 6
class LoggedDF(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        # Copy self to a temporary DataFrame
        temp = self.copy()

        # Create a new column filled with self.created_at
        temp["created_at"] = self.created_at

        # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
        pd.DataFrame.to_csv(temp, *args, **kwargs)
