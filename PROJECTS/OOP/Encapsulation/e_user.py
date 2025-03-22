class BankAccount:
    """
    A simple bank account class demonstrating encapsulation.
    """
    def __init__(self, account_holder, balance=0):
        # Private attributes (Encapsulation)
        self.__account_holder = account_holder  # Name of account holder
        self.__balance = balance  # Private balance attribute

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        """Public method to check balance."""
        return self.__balance

    def get_account_holder(self):
        """Public method to get the account holder's name."""
        return self.__account_holder

# Taking user input for account details
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

# Creating an account with user input
account = BankAccount(name, initial_balance)

# Taking user input for deposit
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

# Taking user input for withdrawal
withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

# Displaying final details
print(f"Account Holder: {account.get_account_holder()}")
print(f"Final Balance: {account.get_balance()}")
