'''
Question 1: Create a Class for Bank Accounts
Create a Python class called BankAccount with the following attributes and methods:

Attributes:

account_number (string): A unique identifier for the account.
balance (float): The current balance of the account.
Methods:

deposit(amount): Adds the specified amount to the balance.
withdraw(amount): Deducts the specified amount from the balance if funds are sufficient; otherwise, print an error message.
display_balance(): Prints the current balance.
Create an instance of BankAccount and perform the following:

Deposit ₹10,000.
Withdraw ₹5,000.
Display the final balance.

'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self,amount):
        print(f"You Added {amount} Rs. to the Account. Your Total Amount is {amount + self.balance}")
    
    def withdraw(self,amount):
        if amount < self.balance:
            print(f"You withdraw {amount} Rs. Your Total Amount is {amount + self.balance}")
        else:
            print(f"Insufficient Fund!")
    def display_balance(self):
        print(f'Your Current Balance is {self.balance}')
    

Customer1 = BankAccount("123456789",20000.50)
Customer1.deposit(10000)
Customer1.withdraw(5000)
Customer1.display_balance()