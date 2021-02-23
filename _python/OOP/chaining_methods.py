'''
Chaining Methods
Objectives:
Understand how to chain methods
In the last assignment, your code might have looked something like this:

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(50)
guido.display_user_balance()
This takes up a lot of space and we're repeating our call to guido many times. 
There is a way to call on guido just once and keep attaching new method calls 
to the end of the previous one, like so:
'''

#guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

'''
This is called chaining. In order for this to work, each method must return self. By returning self, 
if we recall how functions work, each method call will now be equal to the instance that called it.

For example if guido.make_deposit(100) returns its own instance (guido), then we can call one of 
that instance's methods after that call, like guido.make_deposit(100).make_withdrawal(50).
'''

# class User:
#     def make_deposit(self, amount):
#         # your code goes here...
#         return self

'''
The practice of having OOP return its own instance is pretty common and is done in other 
programming languages, though the variable name in some languages is not self, but instead this.
'''
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

    def display_user_balance(self):      
        print("user: " + self.name + ", Balance: $" + str(self.account_balance))


Veries = User("Veries", "veries@me.com")

Margo = User("Margo", "margo@icloud.com")

Frank = User("Frank", "mfrank@gmail.com")


Veries.make_deposit(500).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
Margo.make_deposit(800).make_deposit(200).make_deposit(300).make_withdrawal(250).display_user_balance()
Frank.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(500).display_user_balance()