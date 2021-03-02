# Chaining Methods
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
            # ---------------------------------------------------------|
            # added return statements for chaining
            return self
            
# ---------------------------------------------------------------------|
# Deposit

    def make_deposit(self, amount):
        self.account_balance += amount
        # -------------------------------------------------------------|
            # added return statements for chaining
        return self
        
# ---------------------------------------------------------------------|
# Display Balance

    def display_user_balance(self):      
        print("user: " + self.name + ", Balance: $" + str(self.account_balance))

# ---------------------------------------------------------------------|
# Create User   
Veries = User("Veries", "veries@me.com")

# ---------------------------------------------------------------------|
# Chaining Method  
Veries.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

    

