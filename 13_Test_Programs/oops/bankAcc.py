class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
    
    def print_balance(self):
        print(self.balance)

bankAcc = BankAccount(123456)
bankAcc.deposit(100)
bankAcc.print_balance()