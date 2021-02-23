# Creating a class

# class User:
#     pass # we'll fill this in shortly

'''
And here's how we create a new instance of our class:
'''
# michael = User()
# anna = User()

'''
Over the next few tabs, we'll start fleshing out our User class with:

Attributes: Characteristics shared by all instances of the class type.
Methods: Actions that an object can perform. A user, for example, should 
be able to make a deposit or a withdrawal, or maybe send money to another user.
'''

'''
Attributes
Objectives:

Learn how to set the attributes of a class

'''
#Get familiar with the __init__() method

'''
Let's start building our User class by adding attributes. 
Again, attributes are characteristics of an object. For example, 
in our banking application, we may be interested in their name, email, 
and account balance. Attributes are defined in a "magic method" called 
__init__, which method is called when a new object is instantiated.
'''
# class User:
    # def __init__(self): #The first parameter of every method within a class will be self
    #     self.name = "Michael" #class's attribute names are also indicated by self.
    #     self.email = "michael@codigdojo.com"
    #     self.account_ball = 0

# We'll talk more about self later, but for now just follow this pattern: 
'''
self.<<attribute_name_of_your_choosing>>
'''
# guido = User() # Then to instantiate a couple of new users:
# monty = User()

# print(guido.name) # If we want to access our instance's attributes, we can refer to them from our instances by name:
# print(monty.name)

'''
With the __init__ method's parameters, we indicate what needs to be provided (i.e. arguments) when the class is instantiated.
'''
#(self is always passed in implicitly.)

'''
In our example, even though we have 3 attributes, we only require input for 2 of them. When the User instance 
is created, we should expect to receive specific values for the name and email address. We'll assume, however, 
that everyone starts with $0 in their account. Let's adjust our code to allow arguments to be passed in upon instantiation:
'''
# class User:
#     def __init__(self, name, email_address): # now our method has 2 parameters!
#         self.name = name			# and we use the values passed in to set the name attribute
#         self.email = email_address		# and the email attribute
#         self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

'''

Methods

Objectives

Learn how to add methods to a class
Understand the purpose and meaning of self

'''
# guido.make_deposit(100)
'''
Now it's time to add some functionality to our class. Methods are just functions 
that belong to a class. This means that we can't call them independently as we 
have called functions previously; rather, methods must be called from an instance 
of a class. For example, if a user wanted to make a deposit, we'd want to be able 
to call the method from the user instance; because a specific user is making a deposit, 
it should only affect that user's balance. Making such a call would look something like this:
'''

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

'''
Don't forget that the first parameter of every method within 
a class should be self. Notice that, in addition to whatever 
arguments are passed in as a traditional function, methods also 
have access to the class's attributes.

Now that our method is written, we can call it:
'''
guido = User("guido", "guido@porkchop.com") # Then to instantiate a couple of new users:
monty = User("monty", "guido@porkchop.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

'''
Self
It's probably time to talk about self. The self parameter includes all the 
information about the individual object that has called the method. But how 
does it get passed in? Based on the signature for the deposit method or the 
__init__ method, they require 2 and 3 arguments, respectively. However, when 
we call on them, we pass in only 1 and 2. What's happening here? Because we 
are calling on the method from the instance, this is known as implicit passage 
of self. When we call on a method from an instance, that instance, along with 
all of its information (name, email, balance), is passed in as self.
'''

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