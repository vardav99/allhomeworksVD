class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds")
        else:
            self.balance -= amount

    def print_balance(self):
        print("Account balance:", self.balance)
# Bank account with balance 1000 usd
acct = BankAccount("3156461161", 1000.0)

# Deposit 500.0 into the account
acct.deposit(500.0)

# Print the account balance
acct.print_balance()

# For error message
#acct.withdraw(2000.0)

# Withdraw 700.0 from the account
acct.withdraw(700.0)

# Print the account balance again
acct.print_balance()
