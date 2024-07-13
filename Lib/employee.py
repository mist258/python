from base_book import Book
from lib1 import Library
from lib2 import Library2


class Salary:
    def __init__(self, payment):
        self.valid_payment(payment)

        self.payment = payment

    @classmethod
    def valid_payment(cls, payment):
        if not isinstance(payment, (int, float)):
            raise TypeError('Payment must be of type int or float')

    def get_pay_for_year(self):
        return self.payment * 12


class Employee(Library, Library2,  Book, Salary):

    def __init__(self, payment, bonus):
        super().__init__()
        self.valid_bonus(bonus)

        self.books_from_customer: list = [] # get books returned by customers
        self._salary = Salary(payment)
        self._bonus = bonus

    @classmethod
    def valid_bonus(cls, bonus):
        if not isinstance(bonus, (int, float)):
            raise TypeError('Bonus must be of type int or float')

    def get_salary(self):
        return self._salary.get_pay_for_year() + self._bonus

    def returned_books(self, book):
        self.books_from_customer.append(book)

    @staticmethod
    def delete_book(book_isbn, *args): # delete book from all libraries
        found_book = False
        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if hasattr(book, 'get_book_isbn') and book.get_book_isbn() == book_isbn:
                        lib._books.remove(book)
                        print(f'Deleted book: {book}')
                        found_book = True
                        break  # delete the fist found book
                if found_book:
                    break
        if not found_book:
            raise ValueError(f'Book ISBN {book_isbn} does not exist or invalid')

    @staticmethod
    def find_book(book_isbn, *args): # finds (check availability) the book by ISBN in both libraries
        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if hasattr(book, 'get_book_isbn') and book.get_book_isbn() == book_isbn:
                        print(book)
                        break

    @staticmethod
    def add_book(add_book, *args): # add books to libraries
        for book in args:
            if hasattr(book, '_books'):
                book._books.append(add_book)



