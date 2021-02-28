class BankAccount:
    #                  4.0
    def __init__(self, rate, balance=0):
        # .004
        self.int_rate = (rate * .01)
        self.balance = balance

    def deposit(self, amount):
        # increases the account balance by the given amount
        self.balance += amount

    def withdraw(self, amount):
        # decreases the account balance by the given amount if there are sufficient funds
        amount_after_withdraw = self.balance - amount
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if amount_after_withdraw < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount

    def display_account_info(self):
        # print to the console: eg. "Balance: $100"
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate

        # NOTE: In the video, i forgot to check if balance was above 0
        if self.balance > 0:
            interest_yielded = self.balance * self.int_rate
            self.balance += interest_yielded


BankAccount.deposit(7,500)
