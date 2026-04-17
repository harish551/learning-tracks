'''
Generators in Python are a simple way to create iterators. 
They are functions that return an iterable sequence of values.

Generators use the `yield` statement to produce a value and pause the function's execution,
resuming from the same point when the next value is requested.

Iterators are objects that implement the iterator protocol, 
which consists of the methods `__iter__()` and `__next__()`.
'''

# Example of a simple generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        print(f"Yielded {count}, resuming...")
        count += 1

# Using the generator
iter = count_up_to(5)
print(next(iter))  # Output: 1 
print(next(iter))  # Output: 2
print(next(iter))  # Output: 3
print(next(iter))  # Output: 4
print(next(iter))  # Output: 5
# print(next(iter))  # This will raise StopIteration

for number in count_up_to(3):
    print(f"Received {number} in loop")