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

# Example usage
account = BankAccount("John Doe", 1000)  # Creating an account with an initial balance
account.deposit(500)  # Depositing money
account.withdraw(300)  # Withdrawing money
print(f"Account Holder: {account.get_account_holder()}")  # Getting account holder name
print(f"Final Balance: {account.get_balance()}")  # Checking final balance