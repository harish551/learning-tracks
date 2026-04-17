'''
Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP)
that helps to protect the internal state of an object and restrict direct access to its data.

In Python, encapsulation is achieved through the use of private and protected attributes,
as well as getter and setter methods to control access to these attributes.
'''

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name  # Getter method for name

    def set_name(self, name):
        self.__name = name  # Setter method for name

    def get_age(self):
        return self.__age  # Getter method for age

    def set_age(self, age):
        if age > 0:
            self.__age = age  # Setter method for age with validation
        else:
            raise ValueError("Age must be positive")
        

person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

person.__name = "Bob"
print(person.get_name())  # Output: Alice (name is not changed due to encapsulation)    