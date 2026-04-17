'''
Decorators in Python are a powerful feature that allow you to modify
the behavior of functions or classes without permanently changing their code.

They are essentially functions that take another function as an argument 
and return a modified version of that function.
'''

# Example of a simple decorator
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Example of a decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Example of a cache decorator
def cache(func):
    cached_results = {}
    def wrapper(n):
        if n in cached_results:
            print("Fetching from cache")
            return cached_results[n]
        else:
            print("Calculating result")
            result = func(n)
            cached_results[n] = result
            return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))  # Calculating result
print(fibonacci(10))  # Fetching from cache