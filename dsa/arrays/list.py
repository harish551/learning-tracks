'''
List - Data Structure

A list is an ordered collection of elements.
Stored as a contiguous block of memory where each element is an object.
'''

l = [1, 2, 3, 4, 5]
print(l)
print(type(l))

# Access
print("Element at 0th index: ",l[0])

# Slicing
print("Slicing [1:4]: ",l[1:4])

# Length
print("Length of list: ",len(l))

# Append
print("Append 6: ",l.append(6))
print("List: ",l)

# Remove
print("Remove 6: ",l.remove(6))
print("List: ",l)

# Insert
print("Insert 6 at index 2: ",l.insert(2,6))
print("List: ",l)

# Pop
print("Pop element at index 2: ",l.pop(2))
print("List: ",l)

# Traverse
print("Traverse: ")
for i in l:
    print(i, end=" ")

# Reverse
print("Reverse: ")
l.reverse()
print(l)

# Extend
print("Extend: ")
l.extend([6,7,8])
print(l)

# Copy
print("Copy: ")
l2 = l.copy()
print(l2)


