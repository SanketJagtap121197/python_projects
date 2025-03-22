from abc import ABC, abstractmethod  # Import ABC (Abstract Base Class) and abstractmethod

# Abstract class defining a Bank Account
class BankAccount(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Store account holder name
        self.balance = balance  # Store balance
    
    @abstractmethod  # Abstract method that must be implemented in child classes
    def deposit(self, amount):
        pass

    '''
    # Alternative way to define abstract method
    def deposit(self, amount):
        pass
    deposit = abstractmethod(deposit)  # Explicitly applying the decorator
    '''

    '''
    Why We Write @abstractmethod:
    Ensures Implementation in Subclasses
    If a subclass does not override an abstract method, it cannot be instantiated.
    Defines a Blueprint for Child Classes
    It enforces a structure where every subclass must implement core functionality.
    '''
    
    @abstractmethod  # Abstract method for withdrawal
    def withdraw(self, amount):
        pass
    
    def get_balance(self):  # Concrete method (not abstract) to check balance
        return f"{self.account_holder}'s balance: {self.balance}"
    
'''
We created separate classes for deposit and withdrawal inside SavingsAccount and CurrentAccount because each type of account has different rules for handling these operations.

Why Separate Classes for Deposit and Withdrawal?

Different Business Logic

SavingsAccount has a minimum balance rule (e.g., must maintain ₹500).

CurrentAccount allows withdrawals without a minimum balance.

Encapsulation & Maintainability

Keeping deposit() and withdraw() separate ensures that the logic for each account type remains independent and modular.

If bank rules change (e.g., different minimum balance), we only modify the relevant class.

Following OOP Principles

Abstraction: The base class (BankAccount) defines deposit() and withdraw() as abstract methods, ensuring every account type must implement them.

Polymorphism: Both account types override these methods differently.
'''

'''
savings = SavingsAccount("Alice", 1000)
savings.withdraw(1200)  # ❌ Not allowed (minimum balance required)

current = CurrentAccount("Bob", 2000)
current.withdraw(2500)  # ❌ Not allowed (insufficient funds, but no minimum balance rule)
'''

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

# Example Usage
savings = SavingsAccount("Alice", 1000)  # Create Savings Account object
current = CurrentAccount("Bob", 2000)    # Create Current Account object

savings.deposit(500)  # Deposit into savings account
savings.withdraw(1200)  # Try to withdraw from savings (checks min balance)
print(savings.get_balance())  # Check balance

current.withdraw(2500)  # Withdraw more than balance (should fail)
current.deposit(3000)  # Deposit money
print(current.get_balance())  # Check balance
