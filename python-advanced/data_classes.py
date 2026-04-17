'''
Data classes provide a convenient way to define classes that primarily store data. 
They automatically generate special methods like 
__init__, __repr__, and __eq__ based on the class attributes, 
reducing boilerplate code and improving readability.
'''

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)  # Output: Point(x=1, y=2)
print(p1 == p2)  # Output: True

@dataclass
class Person:
    name: str
    age: int
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
print(person1 == person2)  # Output: True
print(person1)  # Output: Person(name='Alice', age=30)  



class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyClass(x={self.x}, y={self.y})"
    
    def __eq__(self, value):
        if not isinstance(value, MyClass):
            return NotImplemented
        return self.x == value.x and self.y == value.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
my_obj1 = MyClass(1, 2)
my_obj2 = MyClass(1, 2)
print(my_obj1)  # Output: MyClass(x=1, y=2)
print(my_obj1 == my_obj2)  # Output: True


@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

immutable_point1 = ImmutablePoint(3, 4)
#immutable_point1.x = 5  # This will raise a FrozenInstanceError
print(immutable_point1)  # Output: ImmutablePoint(x=3, y=4