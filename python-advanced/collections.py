'''
Collections:

The `collections` module in Python provides specialized container datatypes 
that offer alternatives to Python's general-purpose built-in 
containers like `dict`, `list`, `set`, and `tuple`. 

These specialized containers are designed to provide 
additional functionality and performance benefits for specific use cases.

Some of the most commonly used classes in the `collections` module include:
- `Counter`: A subclass of `dict` for counting hashable objects.
- `defaultdict`: A subclass of `dict` that provides a default value for missing keys.
- `OrderedDict`: A subclass of `dict` that maintains the order of keys as they were added.
- `namedtuple`: A factory function for creating tuple subclasses with named fields.
- `deque`: A list-like container with fast appends and pops on either end.

'''

from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

# Example of using Counter
counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Example of using defaultdict
dd = defaultdict(int)
dd['apple'] += 1
print(dd)  # Output: defaultdict(<class 'int'>, {'apple': 1})

# Example of using OrderedDict
od = OrderedDict()
od['first'] = 2
od['second'] = 2
print(od)  # Output: OrderedDict([('first', 2), ('second', 2)])

# Example of using namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)  # Output: Point(x=1, y=2)
print(p.x)  # Output: 1
print(p.y)  # Output: 2

# Example of using deque
d = deque([1, 2, 3])
d.append(4)  # Add to the right
d.appendleft(0)  # Add to the left
print(d)  # Output: deque([0, 1, 2, 3, 4])
d.pop()  # Remove from the right
d.popleft()  # Remove from the left
print(d)  # Output: deque([1, 2, 3])



