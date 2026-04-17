'''
Function tools for working with functions and callable objects.
This module provides various utilities for working with functions, such as
decorators, partial functions, and function composition.
'''

# wraps is a decorator that helps preserve the original function's metadata when creating a wrapper function.
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Greet the person with the given name."""
    print(f"Hello, {name}!")

say_hello("Alice")
print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: Greet the person with the given


# lru_cache is a decorator that provides a simple way to cache the results of function calls, improving performance for expensive or frequently called functions.
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55
print(fibonacci(20))  # Output: 6765

# reduce is a function that applies a binary function cumulatively 
# to the items of an iterable, reducing the iterable to a single value.

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

summ = reduce(lambda x, y: x + y, numbers, 0)  # Starting with an initial value of 0
print(summ)  # Output: 10