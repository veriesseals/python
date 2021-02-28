# Assignment: User
# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

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

    

