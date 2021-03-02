# Bank Account
# ---------------------------------------------------------------------|
# User

class User():

    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

# ---------------------------------------------------------------------|
# Withdrawal

    def make_withdrawal(self, amount):
        if(self.account_balance < amount):
            print("Insuffienct Funds")
            self.account_balance -=5
        else:
            self.account_balance -= amount
            
# ---------------------------------------------------------------------|
# Deposit
 
    def make_deposit(self, amount):
        self.account_balance += amount
        
# ---------------------------------------------------------------------|
# Display Balance

    def display_user_balance(self):      
        print("user: " + self.name + ", Balance: $" + str(self.account_balance))
        
# ---------------------------------------------------------------------|
# Create Bank Account Class

class BankAccount:
    def __init__(self, int_rate, balance = 0):      
        self.int_rate = int_rate
        self.balance = balance
        
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
        
    def make_withdrawal(self, amount):
        if(self.account_balance < amount):
            print("Insuffienct Funds")
            self.account_balance -=5
        else:
            self.account_balance -= amount
            return self
        
    def display_user_balance(self): 
        print("***********************************")
        print("user: " + self.name + ", Balance: $" + str(self.account_balance))
        print(f'* int_rate is: {self.account_balance}*')
        print("***********************************")
        return self
        
    def yield_interest(self):
        balance *= int_rate
        return self


# ---------------------------------------------------------------------|
# Create User 
Veries = User("Veries", "veries@me.com")

# ---------------------------------------------------------------------|
# Make Deposit

Veries.make_deposit(4000)
Veries.make_deposit(2000)
Veries.make_deposit(300)

# ---------------------------------------------------------------------|
# Withdrawal

Veries.make_withdrawal(4356.76)
Veries.display_user_balance()

# ---------------------------------------------------------------------|
# Other Users with deposits and withdrawals

Judy = User("Judy", "judy@me.com")

# ---------------------------------------------------------------------|
# Make Deposit

Judy.make_deposit(6000)
Judy.make_deposit(1000)
Judy.make_deposit(200)

# ---------------------------------------------------------------------|
# Withdrawal

Judy.make_withdrawal(3200.76)
Judy.display_user_balance()

# ---------------------------------------------------------------------|