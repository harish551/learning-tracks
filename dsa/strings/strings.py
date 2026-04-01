'''
string - Data Structure

A string is a sequence (or array) of characters.
Stored as a contiguous block of memory where each element is a character.
'''

s = "Hello World"
print(s)
print(type(s))

# Access
print(s[0])

# Slicing
print(s[1:4])

# Length
print(len(s))

# Concatenation
print(s + "!")

# Reverse
print(s[::-1])

# Membership
print("l" in s)

# Iteration
for char in s:
    print(char, end=" ")

# Methods
print("lower case: ",s.lower())
print("upper case: ",s.upper())
print("strip: ",s.strip())
print("split: ",s.split())

# Replace
print("replace: ",s.replace("World", "Universe"))

# Find
print("find: ",s.find("World"))

# Count
print("count of 'l': ", s.count("l"))

# StartsWith
print("starts with 'Hello': ",s.startswith("Hello"))

# EndsWith
print("ends with 'World': ",s.endswith("World"))

# Join
print("join words with space: "," ".join(["Hello", "World"]))

# Format
print("format: ","{} {}".format("Hello", "World"))

