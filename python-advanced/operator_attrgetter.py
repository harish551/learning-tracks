'''
operator.attrgetter is a powerful function in Python that allows you to create
a callable object that fetches attributes from its operand.

 It is commonly used for sorting and grouping data based on specific attributes.
'''

from operator import attrgetter

class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Company:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Person:
    def __init__(self, name, age, address, company):
        self.name = name
        self.age = age
        self.address = address
        self.company = company


people = [
    Person("Alice", 30, Address("New York", "NY"), Company("TechCorp", "New York")),
    Person("Bob", 25, Address("San Francisco", "CA"), Company("InnovateX", "San Francisco")),
    Person("Charlie", 35, Address("Chicago", "IL"), Company("DataSolutions", "Chicago")),
    Person("David", 28, Address("New York", "NY"), Company("TechCorp", "New York")),
    Person("Eve", 32, Address("San Francisco", "CA"), Company("InnovateX", "San Francisco"))
]

sort_key = "address.city"

sorted_people = sorted(people, key=attrgetter(sort_key))
print("People sorted by city:")
for person in sorted_people:
    print(f"{person.name} - {person.address.city}")