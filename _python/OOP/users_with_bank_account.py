# Users with Bank Account
# ---------------------------------------------------------------------|
# User

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

# ------------------------------------------------------------------|
# calling the functions for the accounts

    def create_account(self, name, amount, int_rate):
        self.accounts[name]=BankAccount(int_rate, amount)
        print(f'Account {name} successfully created')
        self.accounts[name].display_account_info()
    
    def deposit(self, amount, account_name):
        self.acounts[account_name].deposit(amount)
        
    def withdraw(self, amount, account_name):
        self.acounts[account_name].withdraw(amount)
        

# ------------------------------------------------------------------|
# Printing everything inthe functions by using a for-loop
    def print_info(self):
        print(self.name)
        print(self.email)
        for account_name, account in self.accounts.items():
            accounts.display_account_info()
        

# ---------------------------------------------------------------------|
# Create Bank Account Class (Functionality)

class BankAccount:
    def __init__(self, int_rate, balance = 0):      
        self.int_rate = int_rate
        self.balance = balance
        
    def make_deposit(self, amount):
        self.balance += amount
        return self
        
    def make_withdrawal(self, amount):
        if(self.balance < amount):
            print("Insuffienct Funds")
            self.balance -=5
        else:
            self.balance -= amount
            return self
        
    def display_account_info(self): 
        print("***********************************")
        print(f'* Balance is: {self.balance} *')
        print(f'* int_rate is: {self.balance} *')
        print("***********************************")
        return self
        
    def yield_interest(self):
        self.balance *= self.int_rate
        return self


# ---------------------------------------------------------------------|
# Create User 
Veries = User("Veries", "veries@me.com")

# ---------------------------------------------------------------------|
# Create Accounts
Veries.create_account('checking', '500', .01)
Veries.create_account('savings', '1000', .02)

Veries.print_info()



 