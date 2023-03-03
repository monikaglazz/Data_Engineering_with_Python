

# ex 1
class BankAccount:
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        # return self.number == other.number
        # modification to compare only the same type objects (add in ex 2)
        if type(other) == type(self):
            return (self.number == other.number)
        else:
            return False


# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)


# ex 2
class Phone:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number


acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)


# ex 3
class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True


class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True


p = Parent()
c = Child()

p == c  # returns "Child's __eq__() called and True"


# ex 4
class Employees:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(
            name=self.name, salary=self.salary)
        return s

    def __repr__(self):
        r = "Employee('{name}', {salary})".format(
            name=self.name, salary=self.salary)
        return r


emp1 = Employees("Amar Howard", 30000)
print(emp1)
emp2 = Employees("Carolyn Ramirez", 35000)
print(emp2)


# ex 5
def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))



# ex 6
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
       raise BonusError  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
       raise SalaryError
      
    else:  
      self.salary += amount