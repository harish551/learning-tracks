class BankAccount:

    def __init__(self, account_addr, name, deposit_amount):
        self.account_addr = account_addr
        self.name = name
        self.balance = deposit_amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            return False
            
        self.balance -= amount
        return True
    
    def print_account_details(self):
        print(f'Account Address: {self.account_addr}')
        print(f'Name: {self.name}')
    
    def print_balance(self):
        print('Balance: ', self.balance)



account1 = BankAccount('Acc1', 'Harish', 100)
account1.deposit(100)
account1.print_account_details()
account1.print_balance()

account2 = BankAccount('Acc2', 'Marri', 1000)
account2.withdraw(101)
account2.print_account_details()
account2.print_balance()



