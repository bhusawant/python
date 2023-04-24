# Q.1)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def volume(self):
        pass

class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * 3.14159 * (self.radius ** 3)

class Cube(Shape):
    def __init__(self, length):
        self.length = length

    def volume(self):
        return self.length ** 3



from Mypackage.Shapes.Shape import Sphere, Cube



s = Sphere(2)
print("Volume of sphere with radius 2: ", s.volume())

c = Cube(3)
print("Volume of cube with side length 3: ", c.volume())
