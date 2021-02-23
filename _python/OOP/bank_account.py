
# Assignment: BankAccount
# Objectives
# Practice writing classes
# As we continue thinking about our banking application, we realize that it 
# would be more accurate to assign a balance not to the user directly, but that 
# in the real world, users have accounts, and accounts have balances. This gives
# us the idea that maybe an account is its own class! But as we stated, it is not 
# completely independent of a class; accounts only exist because users open them.

# For this assignment, don't worry about putting any user information in the 
# BankAccount class. We'll take care of that in the next lesson!

# Let's first just get some more practice writing classes by writing a new 
# BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance 
# is created, if an amount is given, the balance of the account should initially 
# be set to that amount; otherwise, the balance should start at $0. The account 
# should also have an interest rate, saved as a decimal (i.e. 1% would be saved 
# as 0.01), which should be provided upon instantiation. (Hint: when using default 
# values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if 
# there are sufficient funds; if there is not enough money, print a message 
# "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance 
# * the interest rate (as long as the balance is positive)
# This means we need a class that looks something like this:

# class BankAccount:
# 	def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
# 		# your code here! (remember, this is where we specify the attributes for our class)
#                 # don't worry about user info here; we'll involve the User class soon
# 	def deposit(self, amount):
# 		# your code here
# 	def withdraw(self, amount):
# 		# your code here
# 	def display_account_info(self):
# 		# your code here
# 	def yield_interest(self):
# 		# your code here


class BankAccount():

    def __init__(self, int_rate, balance):
        self.int_rate = .05
        self.balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):      
        print("user: " + self.name + ", Balance: $" + str(self.account_balance))
        
    def yield_interest(self):      
        print("user: " + self.name + ", Balance: $" + str(self.account_balance))
        
        
BankAccount.make_deposit(5, 400)






