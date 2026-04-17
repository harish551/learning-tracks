'''
Pickle Module

The pickle module in Python is used for serializing and deserializing Python objects. 
Serialization refers to the process of converting 
a Python object into a byte stream, which can then be saved 
to a file or transmitted over a network. 

Deserialization is the reverse process, 
where the byte stream is converted back into a Python object.
'''

import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# Create an instance of the Person class
person = Person("Alice", 30)
# Serialize the person object to a byte stream
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)
# Deserialize the byte stream back to a Person object
with open("person.pkl", "rb") as f:
    deserialized_person = pickle.load(f)
print(deserialized_person.greet())  # Output: Hello, my name is Alice and I am 30 years old.