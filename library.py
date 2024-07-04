#Part 1 BOOK
# *******1.Створити клас Book з відповідними атрибутами  title, author, isbn, copies(У одній бібліотеці), total_copies(По всім бібліотекам).
# 2.Клас повинен мати метод check_availability який буде перевіряти чи є книга у бібліотеці.
# 3.Метод update_total_copies який буде оновлювати загальну кількість копій книжок коли вони будуть змінюватись.
# 4.Метод який буде оновлювати кількість книжок у конкретній бібліотеці(змінювати параметр copies у інстанса).
# *******5.Клас повинен мати метод validate_isbn який буде валідувати правильність isbn коду(ISBN 0-061-96436-0). 	978-3-16-148410-0
#Part 2 LIBRARY
# *******1.Клас Library буде мати поля books, users.
# 2.Методи які дозволять зареєструвати юзера у бібліотеці
# *******3.Методи які дозволять знайти книжку за isbn.
# 4.Методи які дозволять показати всі доступні книжки у бібліотеці.
#*********
#Part 3 USER
# 1.Клас User повинен мати такі атрибути як name, user_id.
# 2.Інфа про функціонал для Customer та Employee, де ви самі повинні розібратись які атрибути де мають бути та як це буде виглядати.
# 3.Атрибути borrowed_books, salary, library.
# 4.Методи для взяття книжки з бібліотеки, та повернення.
# 5.Методи для додавання книжки у бібліотеку та видаленню.
import re
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Book:

    __title: str
    __author: str
    __isbn: str
    __copies: 0 = field(init=False)# only one library
    __total_copies: 0 = field(init=False)# in all available libraries

    def __post_init__(self):
        pattern_isbn = r'^(?:\d{3})-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,7})-(?:\d{1})$' #since 2007 ISBN contains 13 digits
        if not re.fullmatch(pattern_isbn, self.__isbn):
            raise ValueError('Invalid ISBN number')

    def check_availability(self, isbn): # check whether the book is available in library using ISBN
        if self.__isbn != isbn:
            raise ValueError('Invalid ISBN number or ISBN does not exist')
        else:
            self.__copies += 1

    def update_total_copies(self): # update current books copies in all libraries
        pass # total_copies = 0

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f'Book:\nTitle: {self.__title}, Author:{self.__author}, ISBN:{self.__isbn}'


class Library:
    __slots__ = ('books', 'users',)

    def __init__(self,):
        self.books = []
        self.users = []

    def add_initial_books_lst(self, books_lst): # added general list of books
        self.books.extend(books_lst)

    def register_user(self): # delay
        pass

    def show_available_books(self): # show available books in all libraries
        pass


class PublicLibrary(Library, Book):

    def __init__(self): # initialize parent attr 'self.books = []', 'self.users = []'
        super().__init__()

    def update_book_copies(self): # polymorfism
        ...


class PrivateLibrary(Library, Book):
    def __init__(self): # initialize parent attr 'self.books = []', 'self.users = []'
        super().__init__()

    def update_book_copies(self): # polymorfism
        ...


@dataclass(frozen=True)
class User:

    _name: str
    _user_id: int
    _user_email: str

    def salary_for_year(self):
        pass


class Customer(User):
    borrowed_books: list[Book] = []

    def __init__(self, _name, _user_id, _user_email):
        super().__init__(_name, _user_id, _user_email)

    def show_borrowed_books(self): #show all borrowed books
        return f'Borrowed books: {self.borrowed_books}'

    def __str__(self):
        return f'Customer:\nName: {self._name}, User email: {self._user_email}, User id: {self._user_id}, books: {self.borrowed_books}'


class Employee(User):
    pass
# salary, payment


def add_book(self):
    pass
# using append and ISBN


def delete_book(self):
    pass
# using del and ISBN


# cus = Customer('name', 7, 'any.email@gmail.com')
# print(cus)
library_books_lst: list[Book:[]] = [
    ['The Last Wish', 'Andrzej Sapkowski', '978-0-316-05587-6'],
    ['Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7'],
    ['Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0'],
    ['Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7'],
    ['Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7'],
    ['Baptism of Fire', 'Andrzej Sapkowski', '978-0-575-08678-0']]
library = Library()
library.add_initial_books_lst(library_books_lst)
print(library.books)



# def main():
#     pass
#
# if __name__ == '__main__':
#     main()