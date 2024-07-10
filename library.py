#Part 1 BOOK
# *******1.Створити клас Book з відповідними атрибутами  title, author, isbn, copies(У одній бібліотеці), total_copies(По всім бібліотекам).
# 2.Клас повинен мати метод check_availability який буде перевіряти чи є книга у бібліотеці.
# 3.Метод update_total_copies який буде оновлювати загальну кількість копій книжок коли вони будуть змінюватись.
# 4.Метод який буде оновлювати кількість книжок у конкретній бібліотеці(змінювати параметр copies у інстанса).
# *******5.Клас повинен мати метод validate_isbn який буде валідувати правильність isbn коду(ISBN 0-061-96436-0). 	978-3-16-148410-0
#Part 2 LIBRARY
# *******1.Клас Library буде мати поля books, users. # теба створити 2 класи
# *******2.Методи які дозволять зареєструвати юзера у бібліотеці
# *******3.Методи які дозволять знайти книжку за isbn.
# *******4.Методи які дозволять показати всі доступні книжки у бібліотеці.
#*********
#Part 3 USER
# *******1.Клас User повинен мати такі атрибути як name, user_id.
# *******2.Інфа про функціонал для Customer та Employee, де ви самі повинні розібратись які атрибути де мають бути та як це буде виглядати.
# 3.Атрибути borrowed_books, salary, library.
# 4.Методи для взяття книжки з бібліотеки, та повернення.
# *******5.Методи для додавання книжки у бібліотеку та видаленню.
import re
from abc import ABC


class Book:
    __slots__ = ('_title', '_author', '__isbn', '_copies', '_total_copies')

    def __init__(self, title, author, isbn):
        self.valid_isbn(isbn)

        self._title = title
        self._author = author
        self.__isbn = isbn
        self._copies = 0 # only one library
        self._total_copies = 0 # in all available libraries

    @classmethod
    def valid_isbn(cls, isbn): # checks for ISBN validity
        pattern_isbn = r'^(?:\d{3})-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,7})-(?:\d{1})$' #since 2007 ISBN contains 13 digits
        if not re.fullmatch(pattern_isbn, isbn):
            raise ValueError('Invalid ISBN number')

    def get_book_isbn(self):
        return self.__isbn

    def check_availability(self): # check whether the book is available in library using ISBN
        pass

    def update_total_copies(self): # update current books copies in all libraries
        pass # total_copies = 0

    def update_copies(self): #updates copies in only one library
        pass

    def __str__(self):
        return f'Book:\nTitle: {self._title}, Author:{self._author}, ISBN:{self.__isbn}'


class User(ABC):

    __slots__ = ('_name', '_user_id', '_user_email')

    def __init__(self, name, user_id, user_email):

        self._name = name
        self._user_id = user_id
        self._user_email = user_email


class MixinMethodsForManageLibraries:
    def register_user(self, customer: User): # DONE
        if hasattr(self, '_users'):
            if not isinstance(customer, User):
                raise TypeError('Customer must be of type User')
            elif customer not in self._users:
                self._users.append(customer)
            else:
                raise ValueError('Customer already registered')

    def show_available_books(self,):  # show available books in all libraries #DONE
        if hasattr(self, '_books'):
            if self._books is not None:
                for book in self._books:
                    print(book)
            else:
                print('No books available')

    def show_users(self):  # show all users# lib1 = Library() # DONE
        if hasattr(self, '_users'):
            if self._users is not None:
                for user in self._users:
                    print(user)
            else:
                print('Field USERS is empty')


class Library(MixinMethodsForManageLibraries):

    def __init__(self):
        self._users: list[User] = [] # list of all users in lib
        self._books: list = [] # list of all books
        self._borrowed_books: list = [] # show all borrowed books frolm library

    def register_user_in_lib(self, customer: User): # DONE
        self.register_user(customer)

    def show_available_books_in_lib(self):
        self.show_available_books()  # DONE

    def show_users_in_lib1(self): # DONE
        self.show_users()


class Library2(MixinMethodsForManageLibraries):
    def __init__(self):
        self._users: list[User] = [] # list of all users
        self._books: list = [] # list of all books
        self._borrowed_books: list = [] # show all borrowed books from library

    def register_user_in_lib2(self, customer: User): # DONE
        self.register_user(customer)

    def show_available_books_in_lib2(self):
        self.show_available_books() # DONE

    def show_users_in_lib2(self): # DONE
        self.show_users()


class Customer(User):

    def __init__(self, _name, _user_id, _user_email):
        super().__init__(_name, _user_id, _user_email)
        self._borrowed_books: list[Book] = []

    def show_borrowed_books(self): # ?????????????????
        if self._borrowed_books is not None:
            return '\n'.join([f'Title: {book}'for book in self._borrowed_books])
        else:
            return 'No borrowed books'

    def delete_book(self): # equivalent to returning the book
        pass

    def take_book(self): # take book
        pass

    def __str__(self):
        return f'Customer:\nName: {self._name}, user_email: {self._user_email}, user_ID: {self._user_id}'


class Employee(Library, Library2,  Book):

    def __init__(self):
        super().__init__()
        self.borrowed_books: list[Book] = []
        self.salary = 0

    def show_borrowed_books(self): # show all borrowed books ????????????
        if self.borrowed_books is not None:
            for book in self._borrowed_books:
                print(book)
        else:
            print('No borrowed books')

    @staticmethod
    def delete_book(book_isbn, *args): # delete book from all libraries #DONE
        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if hasattr(book, 'get_book_isbn') and book.get_book_isbn() == book_isbn:
                        lib._books.remove(book)
                        print(f'Deleted book: {book}')
                        break  # delete the fist found book
                    elif book.get_book_isbn != book_isbn:
                        raise ValueError(f'Book ISBN {book_isbn} does not exist or invalid')

    @staticmethod
    def find_book(book_isbn, *args): # finds the book by ISBN in both libraries DONE
        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if hasattr(book, 'get_book_isbn') and book.get_book_isbn() == book_isbn:
                        print(book)
                        return book
                    else:
                        raise ValueError('Book not found')

    @staticmethod
    def add_book(add_book, *args): # add books to libraries DONE
        for book in args:
            if hasattr(book, '_books'):
                book._books.append(add_book)

    def employee_salary(self, salary):
        pass


cus = Customer('Anny', 7, 'any.email@gmail.com')
lib1 = Library()
lib2 = Library2()
empl = Employee()
book1 = Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7')
book12 = Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7')
book13 = Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7')
book2 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
book3 = Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')
empl.add_book(book1, lib1, lib2)
empl.add_book(book2, lib2, lib1)
empl.add_book(book3, lib1, lib2)
empl.add_book(book12, lib1)
empl.add_book(book13, lib1)
#print(empl.find_book(book1.get_book_isbn(), lib1, lib2))
#     book = [
#     ['Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7'],
#     ['Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0'],
#     ['Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7'],
#     ['Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7'],
#     ['Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7'],
#     ['Baptism of Fire', 'Andrzej Sapkowski', '978-0-575-08678-0']]
