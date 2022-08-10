

class user():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def display_info(self):
        print(f"User: {self.first_name} {self.last_name}\n Email: {self.email}\n Age: {self.age}\n Is rewards member: {self.is_rewards_member}\n Gold Card Points:{self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("Member is already a rewards member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points - amount >= 0:
            self.gold_card_points -= amount
        else:
            print("Not enough points to spend")
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()

class BankAccount():
    def __init__(self, accountNumber, int_rate, balance):
        self.accountNumber = accountNumber
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

user1,user2, user3  = user('Bruce', 'Wayne', 'iamnotbatman@gmail.com', 62),user('Jason', 'Todd', 'jokersbiggestfan@aol.com', 36), user('Damion', 'Wayne', 'bookytheclown@hotmasil.com', 17)
user1.display_info().enroll().spend_points(50).display_info().enroll()
user2.enroll().spend_points(80).display_info()
user3.display_info().spend_points(40)





