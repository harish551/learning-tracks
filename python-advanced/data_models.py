'''
Data models in Python define the behavior of objects and how they interact with built-in operations.
They are implemented through special methods (also known as magic methods or dunder methods)
that allow you to customize the behavior of your classes and objects.
'''

class A:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"A({self.value})"
    
    def __repr__(self):
        return f"A({self.value})"
    
    def __len__(self):
        pass  # This can be implemented to return the length of the object if applicable

    def __add__(self, other):
        if isinstance(other, A):
            return A(self.value + other.value)
        return NotImplemented
    
a1 = A(10)
a2 = A(20)
print(a1)  # Output: A(10)
print(a2)  # Output: A(20)
a3 = a1 + a2
print(a3)  # Output: A(30)
