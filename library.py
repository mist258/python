# Створіть функціонал для управління бібліотекою. Використовуйте всі набуті знання у ООП для кращого проектування,
# використовуйте атрибути класу та атрибути інстансу, classmethod та staticmethod, приватні та захищені атрибути і так далі.
# Бібліотека повинна мати такі класи: User, Book, Library, Customer, Employee.
# Клас Book повинен мати такі атрибути як: title, author, isbn, copies(У одній бібліотеці), total_copies(По всім бібліотекам).
# Клас повинен мати метод check_availability який буде перевіряти чи є книга у бібліотеці.
# Бібліотека повинна мати такі класи: User, Book, Library, Customer, Employee.
# Метод update_total_copies який буде оновлювати загальну кількість копій книжок коли вони будуть змінюватись.
# Метод який буде оновлювати кількість книжок у конкретній бібліотеці(змінювати параметр copies у інстанса).
# Також клас повинен мати метод validate_isbn який буде валідувати правильність isbn коду(ISBN 0-061-96436-0).
# Клас User повинен мати такі атрибути як name, user_id. Дaлі буде інфа про функціонал для Customer та Employee,
# де ви самі повинні розібратись які атрибути де мають бути та як це буде виглядати. Атрибути borrowed_books, salary, library.
# Методи для додавання книжки у бібліотеку та видаленню. Методи для взяття книжки з бібліотеки, та повернення.
# Клас Library буде мати поля books, users. Методи які дозволять зареєструвати юзера у бібліотеці, знайти книжку за isbn,
# та показати всі доступні книжки у бібліотеці.
# Важливо! Використовуйте все, атрибути класу, атрибути інстансу, клас методи та статик методи, проперті, приватні та протектед атрибути.

import re


class Library:
    __slots__ = ('books', 'users',)

    def __init__(self,):
        self.books = []
        self.users = []

    def update_book_copies(self):
        pass

    def register_user(self): # delay
        pass

    def show_available_books(self):
        pass


class FirstLibrary(Library):

    def __init__(self): # initialize parent attr 'self.books = []', 'self.users = []'
        super().__init__()

    def update_book_copies(self): # polymorfism
        ...


class SecondLibrary(Library):
    def __init__(self): # initialize parent attr 'self.books = []', 'self.users = []'
        super().__init__()

    def update_book_copies(self): # polymorfism
        ...


class Book:
    __slots__ = ('__title', '__author', '__isbn', '__copies', '__total_copies')

    def __init__(self, title, author, isbn):
        self.validate_isbn(isbn)

        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__copies = 0 # only one library
        self.__total_copies = 0 # in all available libraries

    @classmethod
    def validate_isbn(cls, isbn):
        pattern_isbn = r'^(?:\d{3})-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,7})-(?:\d{1})$' #since 2007 ISBN contains 13 digits
        if not re.fullmatch(pattern_isbn, str(isbn)):
            raise ValueError('Invalid ISBN number')

    def check_availability(self): # checks whether the book is available in library
        pass

    def update_total_copies(self): # update current books copies in all libraries
        pass

