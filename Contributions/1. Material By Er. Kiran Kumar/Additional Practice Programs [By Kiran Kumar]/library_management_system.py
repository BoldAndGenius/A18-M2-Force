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
    # books={'chankya':10,'python':50}
    def __init__(self,books):
        self.books = books 
        self.return_book_list = []
    
    sleep(2)
    def add_book(self,book_name):
        print(f"Add books {str(book_name)} to the Library")
        print()
        for book in book_name:
            self.books.append(book)
        # print(self.books)
        sleep(4)
        
    def lend_book(self,book_name):
        if book_name in self.books:
            # print("Debugging")
            print(f'Lend "{book_name}".')
            print()
            self.books.remove(book_name)  #****(missed this function) #list.remove(element)
            # print(self.books) # for debugging
        else:
            print(f'"{book_name}" book is Not Available.')
            print()
        sleep(3)

        
    def return_book(self,book_name):
        print(f'Return "{book_name}".')
        # print()
        self.books.append(book_name)
        # self.return_book_list = []
        self.return_book_list.append(book_name)
        print(f"Return Book List has these {self.return_book_list} Books.")
        print()
        sleep(3)
        
   
books = ['Chanakya Neeti','Bhagwat Geeta','Power of Your Subconscious Mind'] 
Student1 = Library(books)

book_name  = ['Osho', 'Rich Dad Poor Dad']
Student1.add_book(book_name)

Student1.lend_book('Chanakya Neeti')
Student1.lend_book("Python")
Student1.lend_book("Osho")

Student1.return_book("Chanakya Neeti")
Student1.return_book("Osho")















# Improvised Logic 


'''
from time import sleep

class Library:
    def __init__(self, books):
        self.books = books
        self.returned_books = []  # Track returned books
    
    def add_book(self, book_name):
        if isinstance(book_name, list):  # Handle multiple books
            self.books.extend(book_name)
        else:  # Handle a single book
            self.books.append(book_name)
        print(f"Added books: {book_name} to the library.")
        sleep(1)
    
    def lend_book(self, book_name):
        if book_name in self.books:
            print(f'Lending the book: "{book_name}".')
            self.books.remove(book_name)
        else:
            print(f'Sorry, the book "{book_name}" is not available.')
        sleep(1)
    
    def return_book(self, book_name):
        self.books.append(book_name)
        self.returned_books.append(book_name)
        print(f'Returned book: "{book_name}".')
        print(f"Updated Returned Books List: {self.returned_books}")
        sleep(1)

# Example usage
books = ['Chanakya Neeti', 'Bhagwat Geeta', 'Power of Your Subconscious Mind']
library = Library(books)

# Add books
library.add_book(['Osho', 'Rich Dad Poor Dad'])

# Lend books
library.lend_book('Chanakya Neeti')
library.lend_book("Python")
library.lend_book("Osho")

# Return books
library.return_book("Chanakya Neeti")
library.return_book("Osho")



'''