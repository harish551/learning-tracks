'''
Filter function to filter elements from a list based on a condition.
'''

numbers = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]