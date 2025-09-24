from typing import List

# -------------------------
# Book Class
# -------------------------
class Book:
    _total_books = 0   # class variable to track all books
    
    def __init__(self, title: str, author: str):
        self.__title = title          # encapsulated attributes
        self.__author = author
        self.__is_borrowed = False
        Book._total_books += 1
    
    # getters
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def is_borrowed(self):
        return self.__is_borrowed
    
    # methods to borrow/return
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False
    
    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False
    
    @classmethod
    def total_books(cls):
        return cls._total_books
    
    def __str__(self):
        status = "Available" if not self.__is_borrowed else "Borrowed"
        return f"{self.__title} by {self.__author} ({status})"


# -------------------------
# Member Class
# -------------------------
class Member:
    def __init__(self, name: str):
        self.__name = name
        self.__borrowed_books: List[Book] = []   # composition: Member HAS books
    
    def borrow_book(self, book: Book):
        if book.borrow():
            self.__borrowed_books.append(book)
            print(f"{self.__name} borrowed '{book.get_title()}'.")
        else:
            print(f"Sorry, '{book.get_title()}' is already borrowed.")
    
    def return_book(self, book: Book):
        if book in self.__borrowed_books and book.return_book():
            self.__borrowed_books.remove(book)
            print(f"{self.__name} returned '{book.get_title()}'.")
        else:
            print(f"{self.__name} does not have '{book.get_title()}'.")
    
    def list_borrowed_books(self):
        if not self.__borrowed_books:
            print(f"{self.__name} has no borrowed books.")
        else:
            print(f"{self.__name}'s borrowed books:")
            for book in self.__borrowed_books:
                print(f" - {book.get_title()}")


# -------------------------
# Library Class
# -------------------------
class Library:
    def __init__(self, name: str):
        self.__name = name
        self.__books: List[Book] = []         # composition: Library HAS books
        self.__members: List[Member] = []     # composition: Library HAS members
    
    def add_book(self, book: Book):
        self.__books.append(book)
        print(f"Book '{book.get_title()}' added to the library.")
    
    def add_member(self, member: Member):
        self.__members.append(member)
        print(f"Member '{member._Member__name}' registered.")
    
    def list_available_books(self):
        available = [book for book in self.__books if not book.is_borrowed()]
        if not available:
            print("No books available right now.")
        else:
            print("Available books:")
            for book in available:
                print(f" - {book}")
    
    def total_books(self):
        return Book.total_books()


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    # Create a library
    my_library = Library("City Library")
    
    # Add books
    b1 = Book("1984", "George Orwell")
    b2 = Book("The Hobbit", "J.R.R. Tolkien")
    b3 = Book("Python 101", "Michael Driscoll")
    
    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.add_book(b3)
    
    # Add members
    alice = Member("Alice")
    bob = Member("Bob")
    
    my_library.add_member(alice)
    my_library.add_member(bob)
    
    # Borrow & Return
    my_library.list_available_books()
    alice.borrow_book(b1)
    bob.borrow_book(b1)  # already borrowed
    bob.borrow_book(b2)
    my_library.list_available_books()
    
    alice.return_book(b1)
    my_library.list_available_books()
    
    # Track borrowed books per member
    alice.list_borrowed_books()
    bob.list_borrowed_books()
    
    # Track total books created
    print("Total books in system:", my_library.total_books())
