# Walrus operator (:=) allows assignment and return of a value in the same expression.
# Introduced in Python 3.8, it can simplify code by reducing the need 
# for temporary variables and making certain constructs more concise.

# Example 1: Using walrus operator in a while loop
n = 0
while (n := n + 1) < 5:
    print(n)

# Example 2: Using walrus operator in an if statement
s = "Hello, World!"
if (length := len(s)) > 10:
    print(f"String is too long ({length} characters)")
