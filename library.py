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
from abc import ABC, abstractmethod
from email_validator import validate_email, EmailNotValidError


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def update_book_copies(self):
        pass

    def register_user(self):
        pass



class FirstLibrary(Library):
    pass


class SecondLibrary(Library):
    pass


class Book:
    __slots__ = ('title', 'author', '__isbn', 'copies', 'total_copies')

    def __init__(self, title, author, isbn):
        self.validate_isbn(isbn)

        self.title = title
        self.author = author
        self.__isbn = isbn
        self.copies = 0 # only one library
        self.total_copies = 0 # in all available libraries

    @classmethod
    def validate_isbn(cls, isbn):
        pattern_isbn = r'^(?:\d{3})-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,7})-(?:\d{1})$' #since 2007 ISBN contains 13 digits
        if not re.fullmatch(pattern_isbn, str(isbn)):
            raise ValueError('Invalid ISBN number')

    def check_availability(self): # checks whether the book is available in library
        pass

    def update_total_copies(self): # update current books copies in all libraries
        pass


class User:
    def __init__(self, name, user_id, email, phone_numer):
        self.validate_email(email)

        self.__name = name
        self.__user_id = user_id
        self.__email = email
        self.__phone_number = phone_numer

    @classmethod
    def validate_email(cls, email):
        try:
            valid = validate_email(email)
            return valid.email
        except:
            raise EmailNotValidError('Invalid email')


class Customer(User):
    def __init__(self, name, user_id, email, phone_number):
        super().__init__(name, user_id, email, phone_number)
        self.borrowed_books = []

    def __str__(self):
        return f'Customer:\nName: {self.__name}, Id: {self.__user_id}, Email: {self.__email}, Phone number: {self.__phone_number}'


class Employee(User):
    def __init__(self, name, user_id, email, phone_number, salary):
        super().__init__(name, user_id, email, phone_number)
        self.salary = salary



