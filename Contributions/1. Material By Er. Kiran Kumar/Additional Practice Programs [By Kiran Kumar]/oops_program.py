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











'''

Question 2: Build a Library Management System
Write a class Library with the following functionality:

Attributes:

books (list): A list of books available in the library.


Methods:

add_book(book_name): Adds a book to the library.

lend_book(book_name): Lends a book to a user. Remove it from the list if available; otherwise, print a message that the book is not available.

return_book(book_name): Adds the returned book back to the list.

Simulate the following actions using the class:

Add books "Python Basics" and "Data Structures" to the library.
Lend "Python Basics".
Return "Python Basics".
Display the remaining books in the library.


'''

from time import sleep
class Library:
    def __init__(self,books):
        self.books = books 
    
    # sleep(1)
    def add_book(self,book_name):
        print(f"Add books {str(book_name)} to the Library")
        for book in book_name:
            self.books.append(book)
        # print(self.books)
        sleep(2)
        
    def lend_book(self,book_name):
        if book_name in self.books:
            # print("Debugging")
            print(f'Lend "{book_name}".')
            self.books.remove(book_name)  #****(missed this function) #list.remove(element)
            # print(self.books) # for debugging
        else:
            print("Book is Not Available.")
        sleep(2)

        
    def return_book(self,book_name):
        print(f'Return "{book_name}".')
        self.books.append(book_name)
        self.return_book_list = []
        self.return_book_list.append(book_name)
        print(f"Return Book List has these {self.return_book_list} Books.")
        sleep(2)
        
   
books = ['Chanakya Neeti','Bhagwat Geeta','Power of Your Subconscious Mind'] 
Student1 = Library(books)

book_name  = ['Osho', 'Rich Dad Poor Dad']
Student1.add_book(book_name)

Student1.lend_book('Chanakya Neeti')
Student1.lend_book("Python")
Student1.lend_book("Osho")

Student1.return_book("Chanakya Neeti")
Student1.return_book("Osho")
