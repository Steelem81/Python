class BankAccount():

    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance  <= 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1, account2 = BankAccount(100, .3), BankAccount(500, .1)

account1.deposit(20).deposit(100).deposit(100).withdraw(20).yield_interest().display_account_info()
account2.deposit(80).deposit(400).withdraw(30).withdraw(100).withdraw(20).withdraw(50).yield_interest().display_account_info()


