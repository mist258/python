# Створіть функціонал для управління бібліотекою.
# Бібліотека повинна мати такі класи: User, Book, Library, Customer, Employee.
# Клас Book повинен мати такі атрибути як: title, author, isbn, copies(У одній бібліотеці), total_copies(По всім бібліотекам).
# Клас повинен мати метод check_availability який буде перевіряти чи є книга у бібліотеці.
# Метод update_total_copies який буде оновлювати загальну кількість копій книжок коли вони будуть змінюватись.
# Метод який буде оновлювати кількість книжок у конкретній бібліотеці(змінювати параметр copies у інстанса).
# Також клас повинен мати метод validate_isbn який буде валідувати правильність isbn коду(ISBN 0-061-96436-0).
# Клас User повинен мати такі атрибути як name, user_id.
# ДАлі буде інфа про функціонал для Customer та Employee, де ви самі повинні розібратись які атрибути де мають бути та як це буде виглядати.
# Атрибути borrowed_books, salary, library. Методи для додавання книжки у бібліотеку та видаленню.
# Методи для взяття книжки з бібліотеки, та повернення.
# Клас Library буде мати поля books, users.
# Методи які дозволять зареєструвати юзера у бібліотеці, знайти книжку за isbn, та показати всі доступні книжки у бібліотеці.
import re
from abc import ABC


class Book:
    __slots__ = ('_title', '_author', '__isbn')

    _copies: int = 0  # only one library
    _total_copies = 0  # in all available libraries

    def __init__(self, title: str, author: str, isbn: str):
        self.valid_isbn(isbn)

        self._title = title
        self._author = author
        self.__isbn = isbn


    @classmethod
    def valid_isbn(cls, isbn: str): # checks for ISBN validity
        pattern_isbn = r'^(?:\d{3})-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,7})-(?:\d{1})$' #since 2007 ISBN contains 13 digits
        if not re.fullmatch(pattern_isbn, isbn):
            raise ValueError('Invalid ISBN number')

    def get_book_isbn(self):
        return self.__isbn

    def get_book_title(self):
        return self._title

    @staticmethod
    def check_availability(book_isbn, *args): # check whether the book is available in library using ISBN
        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if book_isbn == book.get_book_isbn():
                        print(f'Book \'{book._title}\' is available in libraries')

    @staticmethod
    def update_total_copies(book_isbn, *args): # update current book copies in all libraries

        found_copies = False

        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if book_isbn == book.get_book_isbn():
                        Book._total_copies += 1
                        found_copies = True

        if not found_copies:
            raise ValueError(f'Book not found')
        return Book._total_copies

    @staticmethod
    def update_copies(book_isbn, library): # updates copies in only one library

        found_copy = False
        if hasattr(library, '_books'):
            for book in library._books:
                if book_isbn == book.get_book_isbn():
                    Book._copies += 1
                    found_copy = True

        if not found_copy:
            raise ValueError(f'Book not found')
        return Book._copies

    def __str__(self):
        return f'Book:\nTitle: {self._title}, Author:{self._author}, ISBN:{self.__isbn}'


class User(ABC):

    __slots__ = ('_name', '_user_id', '_user_email')

    def __init__(self, name, user_id, user_email):

        self._name = name
        self._user_id = user_id
        self._user_email = user_email


class MixinMethodsForManageLibraries:
    def register_user(self, customer: User): # registration users in library
        if hasattr(self, '_users'):
            if not isinstance(customer, User):
                raise TypeError('Customer must be of type User')
            elif customer not in self._users:
                self._users.append(customer)
            else:
                raise ValueError('Customer already registered')

    def show_available_books(self,):  # show available books in all libraries
        if hasattr(self, '_books'):
            if self._books is not None:
                for book in self._books:
                    print(book)
            else:
                print('No books available')

    def show_users(self):  # show all users
        if hasattr(self, '_users'):
            if self._users is not None:
                for user in self._users:
                    print(user)
            else:
                print('Field USERS is empty')

    def give_book_for_customer(self, customer_id: User, book_title): # give book for customer from library

        found_cust = None
        found_book = None

        if hasattr(self, '_users'):
            for user in self._users:
                if hasattr(user, '_user_id'):
                    if user._user_id == customer_id:
                        found_cust = user
                    break
        if found_cust is None:
            raise ValueError('Customer not registered')

        if hasattr(self, '_books'):
            for book in self._books:
                if hasattr(book, '_title') and book._title == book_title:
                    found_book = book
                    break

        if found_book is None:
            raise ValueError('Book does not in library')

        found_cust._borrowed_books.append(found_book)


class Library(MixinMethodsForManageLibraries):

    def __init__(self):
        self._users: list[User] = [] # list of all users in lib
        self._books: list = [] # list of all books
        self._borrowed_books: list[Book] = []

    def register_user_in_lib(self, customer: User):
        self.register_user(customer)

    def show_available_books_in_lib(self):
        self.show_available_books()

    def show_users_in_lib1(self):
        self.show_users()

    def give_book_for_customer_lib1(self, customer_id, book_title):
        self.give_book_for_customer(customer_id, book_title)


class Library2(MixinMethodsForManageLibraries):
    def __init__(self):
        self._users: list = [] # list of all users
        self._books: list = [] # list of all books
        self._borrowed_books: list[Book] = []

    def register_user_in_lib2(self, customer: User):
        self.register_user(customer)

    def show_available_books_in_lib2(self):
        self.show_available_books()

    def show_users_in_lib2(self):
        self.show_users()

    def give_book_for_customer_lib2(self, customer_id, book_title):
        self.give_book_for_customer(customer_id, book_title)


class Customer(User):

    removed_books = []

    def __init__(self, _name, _user_id, _user_email):
        super().__init__(_name, _user_id, _user_email)
        self._borrowed_books: list = []

    def show_borrowed_books(self): # show books borrowed by customers
        if self._borrowed_books is not None:
            for book in self._borrowed_books:
                return book

    def delete_book(self, book_title): #
        for book in self._borrowed_books:
            if book._title == book_title:
                self.removed_books.append(book)
                self._borrowed_books.remove(book)
                break

    @staticmethod
    def return_book(*args): # return book to lib
        for lib in args:
            if hasattr(lib, '_books'):
                if Customer.removed_books is not None:
                    for book in Customer.removed_books:
                        lib._books.append(book)
                        break

    def __str__(self):
        return f'Customer:\nName: {self._name}, user_email: {self._user_email}, user_ID: {self._user_id}'


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
        return self._salary.get_pay_for_year() * self._bonus

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
    def find_book(book_isbn, *args): # finds the book by ISBN in both libraries
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

#sequence of method calls

book1 = Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7')
book12 = Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')
book13 = Book('Baptism of Fire', 'Andrzej Sapkowski', '978-0-575-08678-0')
book2 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
book4 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
book5 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
book3 = Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')
cust1 = Customer('Anny', 1, 'any.email@gmail.com')
cust2 = Customer('Mark', 2, 'mark.email@gmail.com')
cust3 = Customer('Nick', 3, 'nick.email@gmail.com')
cust4 = Customer('Sam', 4, 'sam.email@gmail.com')
lib1 = Library()
lib1.register_user(cust1)
lib1.register_user(cust2)
lib2 = Library2()
lib2.register_user(cust3)
lib2.register_user(cust4)
#print(lib1.show_users_in_lib1())
#print(lib2.show_users_in_lib2())
empl = Employee(45, 5)
#print(empl.get_salary())
empl.add_book(book1, lib1, lib2)
empl.add_book(book2, lib1, lib2)
empl.add_book(book3, lib1, lib2)
empl.add_book(book12, lib1)
empl.add_book(book13, lib1)
empl.add_book(book4, lib1)
empl.add_book(book5, lib1)
#empl.find_book('978-0-575-08636-0', lib1, lib2)
#empl.find_book('978-0-575-08678-0', lib1, lib2)
#print(lib1.show_available_books_in_lib())
#print(lib2.show_available_books_in_lib2())
lib1.give_book_for_customer_lib1(1, 'Sword of Destiny')
lib2.give_book_for_customer_lib2(3, 'Time of Contempt')
#empl.delete_book('978-0-575-08637-7', lib1, lib2)
#cust1.delete_book('Sword of Destiny')
#print(cust1.show_borrowed_books())
#print(cust3.show_borrowed_books())
#print(empl.find_book(book1.get_book_isbn(), lib1, lib2))
#check_available = Book.check_availability('978-0-316-27805-7', lib2, lib1)
#print(Book.update_total_copies('978-0-575-08636-0', lib1, lib2))
#print(Book.update_copies('978-0-575-08636-0', lib2))
cust1.delete_book('Sword of Destiny')
cust1.return_book(lib2)
