# Q.1)
"""
class point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, obj2):
        x= self.x+obj2.x
        y= self.y+obj2.y
        return point(x, y)

    def __sub__(self, obj2):
        x= self.x-obj2.x
        y= self.y-obj2.y
        return point(x, y)

    def __lt__(self, obj2):
        if((( self.x**2+self.y** 2)**0.5)<((obj2.x** 2+obj2.y** 2)**0.5)):
            return True
        else:
            return False

    def __gt__(self, obj2):
        if(((self.x**2+self.y**2)**0.5)>((obj2.x** 2+obj2.y** 2)* 0.5)):
            return True
        else:
            return False

    def __str__(self):
        return ("X co-ordinate: {} Y co-ordinate: {} ".format(self.x, self.y))

p1 = point(1, 1)
p2 = point(2, 2)

print(p1.__add__(p2))
print(p2.__sub__(p1))

print(p1.__lt__(p2))
print(p1.__gt__(p2))
print(p1.__str__())
print(p2.__str__())
"""

# print(f"{p1}\n{p2}")



# Q.2)

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def calculate(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    def display(self):
        print(f"Employee Class: {self.emp_class}")
        print(f"Salary: {self.calculate()}")
        print(f"Years of Service: {self.years_of_service}")

class Customer(Bank):
    def __init__(self, account_type, balance):
        self.account_type = account_type.lower()
        self.balance = balance

    def calculate(self):
        if self.account_type == 'savings':
            self.balance += self.balance * 0.04
        elif self.account_type == 'current':
            self.balance += self.balance * 0.06
        else:
            return 0

    def update(self):
        if self.balance > 100000:
            self.balance += self.balance * 0.05
            
    def display(self):
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

class Employee(Bank):
    def __init__(self, emp_class, basic_salary, years_of_service):
        self.emp_class = emp_class
        self.basic_salary = basic_salary
        self.years_of_service = years_of_service

    def calculate(self):
        if self.emp_class == 1:
            gross_salary = self.basic_salary + (self.basic_salary * 0.1215) + (self.basic_salary * 0.3)
            return gross_salary
        elif self.emp_class == 2:
            gross_salary = self.basic_salary + (self.basic_salary * 0.115) + (self.basic_salary * 0.3)
            return gross_salary
        else:
            return 0

    def update(self):
        if self.years_of_service > 15:
            self.basic_salary += self.basic_salary * 0.2
            
customer = Customer("Savings", 500000)
customer.display()        
customer.calculate()
customer.update()
customer.display() 

emp1 = Employee(1, 30000, 20)
emp1.calculate()
emp1.update()
emp1.display()
