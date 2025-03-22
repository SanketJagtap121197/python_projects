from abc import ABC, abstractmethod  # Import ABC (Abstract Base Class) and abstractmethod

# Abstract class defining a Bank Account
class BankAccount(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Store account holder name
        self.balance = balance  # Store balance
    
    @abstractmethod  # Abstract method that must be implemented in child classes
    def deposit(self, amount):
        pass
    
    @abstractmethod  # Abstract method for withdrawal
    def withdraw(self, amount):
        pass
    
    def get_balance(self):  # Concrete method (not abstract) to check balance
        return f"{self.account_holder}'s balance: {self.balance}"

# Concrete class for Savings Account
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount  # Add amount to balance
        print(f"Deposited {amount} in Savings Account. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance - amount >= 500:  # Maintain minimum balance
            self.balance -= amount
            print(f"Withdrawn {amount} from Savings Account. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance! Minimum balance of 500 required.")

# Concrete class for Current Account
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount  # Add deposit amount to balance
        print(f"Deposited {amount} in Current Account. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:  # No minimum balance required
            self.balance -= amount
            print(f"Withdrawn {amount} from Current Account. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance!")

# Function to interact with user
def user_actions(account):
    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print(account.get_balance())
        elif choice == "4":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

# Example Usage
account_type = input("Enter account type (savings/current): ").strip().lower()
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

if account_type == "savings":
    account = SavingsAccount(name, balance)
elif account_type == "current":
    account = CurrentAccount(name, balance)
else:
    print("Invalid account type! Exiting.")
    exit()

user_actions(account)