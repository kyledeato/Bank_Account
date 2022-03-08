class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0):
    # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}" )
        return self
    
    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self

tina = BankAccount(balance=500)
godrick = BankAccount(balance=9999999999)

tina.deposit(400).deposit(200).deposit(50).withdraw(25).yield_interest().display_account_info()
godrick.deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()