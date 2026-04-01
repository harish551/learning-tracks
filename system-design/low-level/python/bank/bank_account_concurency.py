from threading import Thread, Lock, RLock
class BankAccount:

    def __init__(self, account_addr, name, deposit_amount):
        self.account_addr = account_addr
        self.name = name
        self.balance = deposit_amount
        self.lock = Lock()
        self.rlock = RLock()
    
    def deposit(self, amount):
        with self.lock:
            self.balance += amount
    
    def withdraw(self, amount):
        with self.lock:
            if self.balance < amount:
                return False
            
            self.balance -= amount
            return True
    
    def print_account_details(self):
        print(f'Account Address: {self.account_addr}')
        print(f'Name: {self.name}')
    
    def print_balance(self):
        with self.rlock:
            print('Balance: ', self.balance)



if __name__ == "__main__":

    
    account1 = BankAccount('Acc1', 'Harish', 100)
    account2 = BankAccount('Acc2', 'Marri', 1000)
    account2.deposit(10000)

    threads1 = []
    threads2 = []
    
    for _ in range(100):
        t1 = Thread(target=account1.deposit, args=(100,))
        t2 = Thread(target=account2.withdraw, args=(100,))
        threads1.append(t1)
        threads2.append(t2)

        t1.start()
        t2.start()

    for t1, t2 in zip(threads1, threads2):
        t1.join()
        t2.join()
    
    account1.print_account_details()
    account1.print_balance()

    account2.print_account_details()
    account2.print_balance()





