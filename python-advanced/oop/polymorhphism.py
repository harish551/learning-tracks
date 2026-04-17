'''
Polymorphism is another fundamental concept in Object-Oriented Programming (OOP)

polymorphism means "many forms" -- the same interface or method can behave differently 
based on the object that is calling it.

In Python, polymorphism is achieved through method overriding,
where a subclass provides a specific implementation of a method that is already defined in its parent class.
'''

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # Area of a circle
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Area of a rectangle

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"The area is: {shape.area()}")  # Polymorphic call to area() method
    
