'''
Inheritance is a fundamental concept in Object-Oriented Programming (OOP)
that allows a class to inherit properties and methods from another class.

In Python, inheritance is implemented by defining a new class (called a child or subclass)
that derives from an existing class (called a parent or superclass). 

The child class can access all the public methods and attributes
of the parent class and can also define its own methods and attributes.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} barks: Woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} the {self.color} cat meows: Meow!"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.speak())  # Output: Buddy the Golden Retriever barks: Woof!
print(cat.speak())  # Output: Whiskers the Orange cat meows: Meow!