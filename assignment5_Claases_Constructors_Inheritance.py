# Q.1)
"""
class Employee:
    def __init__(self, first_name, last_name, age, basic_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.basic_salary = basic_salary
        self.email = f"{first_name.capitalize()}.{last_name.capitalize()}@gmail.com"
    def calculate_salary(self):
        return self.basic_salary

class Developer(Employee):
    def __init__(self, first_name, last_name, age, basic_salary, language):
        super().__init__(first_name, last_name, age, basic_salary)
        self.language =language

class Manager(Employee):
    def __init__(self, first_name, last_name, age, basic_salary):
        super().__init__(first_name, last_name, age, basic_salary)
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)
        print(f"{subordinate.first_name.capitalize()} {subordinate.last_name.capitalize()} added as subordinate.")

    def display_subordinates(self):
        if not self.subordinates:
            print("No subordinates are monitored by the manager")

        else:
            print("Subordinates of the manager: ")
            for subordinate in self.subordinates:
                print(subordinate.first_name.capitalize(), subordinate.last_name.capitalize())


dev = Developer("Bhuvan", "Sawant", 20, 80000, "Python")
mgr = Manager("Jane", "Smith", 35, 90000)
print(f"Developer Info:\nName:{dev.first_name, dev.last_name}\nAge:{dev.age}\nEmail:{dev.email}")
print("Salary:", dev.calculate_salary())
print(f"\nManager Info:\nName:{mgr.first_name, mgr.last_name}\nAge:{mgr.age}\nEmail:{mgr.email}\nSalary:{mgr.calculate_salary()}")

mgr.add_subordinate(dev)
mgr.display_subordinates()
"""


# Q.2)

class Vehicle:
    def __init__(self, milage, max_speed, name):
        self.milage = milage
        self.max_speed = max_speed
        self.name = name

    def seating_capacity(self):
        pass

    def fare(self):
        fare = 20*self.seating_capacity()
        fare = fare + (0.1*fare)
        return fare

    def vehicle_info(self):
        print("Milage:", self.milage)
        print("Max speed:", self.max_speed)
        print("seating capacity:", self.seating_capacity())
        print("Fare:", self.fare())


class Bus(Vehicle):
    def seating_capacity(self):
        return 40
    

class Car(Vehicle):
    def seating_capacity(self):
        return 4
    

bus = Bus(15, 80, "Best")
car = Car(20, 100, "Mercedes")

print("Bus Info:")
bus.vehicle_info()

print("Car Info:")
car.vehicle_info()


