
class User():

    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def add_intrest(self, amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):      
        print("user: " + self.name + ", Balance: $" + str(self.account_balance))

    
Veries = User("Veries", "veries@me.com")
Veries.make_deposit(4000)
Veries.make_deposit(2000)
Veries.make_deposit(300)
Veries.make_withdrawal(4356.76)
Veries.display_user_balance()


# Margo = User("Margo", "margo@icloud.com")
# Margo.make_deposit(8000)
# Margo.make_deposit(40)
# Margo.make_withdrawal(1000)
# Margo.make_withdrawal(34)
# Margo.display_user_balance()

# Festus = User("Festus", "festus@gmail.com")
# Festus.make_deposit(500)
# Festus.make_withdrawal(30)
# Festus.make_withdrawal(200)
# Festus.make_withdrawal(58)
# Festus.display_user_balance()

    

