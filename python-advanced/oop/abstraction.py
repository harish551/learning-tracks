'''
Abstraction is one of the fundamental principles of Object-Oriented Programming (OOP)

that involves hiding the complex implementation details of an object 
and exposing only the essential features or functionalities.

In Python, abstraction can be achieved using abstract base classes (ABCs) from the `abc` module,
which allows you to define abstract methods that must be implemented by any subclass.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to calculate area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # Implementation of area for Circle

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Implementation of area for Rectangle
    
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of Circle: {circle.area()}")  # Output: Area of Circle: 78.5
print(f"Area of Rectangle: {rectangle.area()}")  # Output: Area of Rectangle: 24

# use shape without knowing the specific type of shape
def print_area(shape):
    print(f"The area is: {shape.area()}")

print_area(circle)  # Output: The area is: 78.5
print_area(rectangle)  # Output: The area is: 24