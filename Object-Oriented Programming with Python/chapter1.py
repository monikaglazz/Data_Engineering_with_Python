from datetime import datetime


class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

        self.hire_date = datetime.today()

    # def set_name(self, new_name):
    #     self.name = new_name

    # def set_salary(self, new_salary):
    #     self.salary = new_salary

    def give_raise(self, amount):
        self.salary = self.salary + amount

    def monthly_salary(self):
        return self.salary / 12


# ex 1
mystery = Employee()

# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)


# ex 2
# Create an object emp of class Employee
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)


# ex 3
# get salary
print(emp.salary)

# give a raise
emp.give_raise(1500)

# get salary
print(emp.salary)


# ex 4
# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)


# ex 5
# Make __init__ and resign from set_name and set_salary methods
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

# ex 6


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x*self.x + self.y*self.y)**0.5

    def reflect(self, axis):
        if axis == 'x':
            self.y = -1 * self.y
        elif axis == 'y':
            self.x = -1 * self.x
        else:
            print("Incorect axis!")


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
