'''
Static and Class Methods

staticmethod and classmethod are decorators in Python 
that define methods that are not bound to an instance of the class.

- staticmethod: A static method does not receive an implicit first argument (like self or cls).
  It behaves like a regular function but belongs to the class's namespace.
- classmethod: A class method receives the class as the implicit first argument (cls)
  and can access class-level attributes and methods.
'''

class MyClass:
    class_variable = "I am a class variable"

    @staticmethod
    def static_method():
        return "This is a static method. It does not have access to the class or instance."
    
    @classmethod
    def class_method(cls):
        return f"This is a class method. It has access to the class variable: {cls.class_variable}"
    
print(MyClass.static_method())  # Output: This is a static method. It does not have access to the class or instance.
print(MyClass.class_method())   # Output: This is a class method. It has access to the class variable: I am a class variable


class BankAccount:
    interest_rate = 0.05  # Class variable representing the interest rate

    def __init__(self, account_type, balance):
        self.account_type = account_type  # Instance variable representing the account type
        self.balance = balance  # Instance variable representing the account balance

    
    @classmethod
    def create_savings_account(cls, initial_deposit):
        '''Factory method to create a savings account with an initial deposit.'''
        if not cls.is_valid_transaction(initial_deposit):
            raise ValueError("Invalid initial deposit amount.")
        return cls("savings", initial_deposit)

    @classmethod
    def create_business_account(cls, initial_deposit):
        '''Factory method to create a business account with an initial deposit.'''
        if not cls.is_valid_transaction(initial_deposit):
            raise ValueError("Invalid initial deposit amount.")
        return cls("business", initial_deposit)
        
    @staticmethod
    def is_valid_transaction(amount):
        return amount > 0  # Static method to validate transaction amount
    
    @staticmethod
    def is_valid_account_type(account_type):
        return account_type in ["savings", "business"]  # Static method to validate account type

    @staticmethod
    def calculate_interest(amount):
        return amount * BankAccount.interest_rate  # Accessing class variable from static method
    
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate  # Modifying class variable from class method

# Example usage
savings_account = BankAccount.create_savings_account(1000)
business_account = BankAccount.create_business_account(5000)

print(savings_account.account_type)  # Output: savings
print(savings_account.balance)       # Output: 1000
print(business_account.account_type)  # Output: business
print(business_account.balance)       # Output: 5000