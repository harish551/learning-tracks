
def validate(data, *validators):
    for validator in validators:
        if not validator(data):
            return False
    return True 

is_non_empty = lambda s: bool(s.strip())
is_alpha = lambda s: s.isalpha()

input_data = 'Hello, World!'
is_valid = validate(input_data, is_non_empty, is_alpha)
print(is_valid)  # Output: False (because of the comma and space)

input_data = 'HelloWorld'
is_valid = validate(input_data, is_non_empty, is_alpha)
print(is_valid)  # Output: True (because it is non-empty and contains only alphabet