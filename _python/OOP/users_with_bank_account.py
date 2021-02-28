
# Create Parent Class: User

# ------------------------------------------------------------------------------------|
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Method for User
# ------------------------------------------------------------------------------------|

    def show_details(self):
        print ("Persoanl Details")
        print ("")
        print ("Name", self.name)
        print ("Age", self.age)
        print ("Gender", self.gender)

# Create Child Class: Bank
# We use inheritance here. It will inherite the information from our user class to the Bank Class.  
# ------------------------------------------------------------------------------------|

class Bank(User):
    def __init__(self, name,  age, gender):
        # We will use a super function to use all of the details already created to keep from having to
        # recode it.
        # ----------------------------------------------------------------------------|
        super().__init__(name, age , gender)
        
        # details about the account balance. The balance should start a 0
        # ----------------------------------------------------------------------------|
        self.balance = 0
        
        # Deposit
        # ----------------------------------------------------------------------------|
        def deposit(self, amount):
            self.amount = amount
            self.balance = self.balance + self.amount
            print("Account balance has been updated : $", self.balance)
            
        # Withdrawal
        # ----------------------------------------------------------------------------|
        def withdraw(self, amount):
            self.amount = amount
            
            # Adding a self check feature to check for over drawing the amount in the account
            # using a conditional statement
            # ------------------------------------------------------------------------|
            if self.amount > self.balance:
                print("Insufficient Funds | Balance Availble : $", self.balance)
            else:
                self.balance = self.balance - self.amount
                print("Account balance has been updated : $", self.balance)
                
        # View Account Balance
        # ----------------------------------------------------------------------------|
        
        def view_balance(self):
            self.show_details()
            print("Account balance: $", self.balance)
                
                
            
         



