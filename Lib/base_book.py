import re


class Book:

    __slots__ = ('_title', '_author', '__isbn', 'copies')

    _total_copies = None  # in all available libraries or one lib

    def __init__(self, title: str, author: str, isbn: str):
        self.valid_isbn(isbn)

        self._title = title
        self._author = author
        self.__isbn = isbn
        self.copies = 0  # books copies in one library

    @classmethod
    def valid_isbn(cls, isbn: str):  # checks for ISBN validity
        pattern_isbn = r'^(?:\d{3})-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,7})-(?:\d{1})$'  # since 2007 ISBN contains 13 digits
        if not re.fullmatch(pattern_isbn, isbn):
            raise ValueError('Invalid ISBN number')

    def check_availability(self):  # check books availability in a certain library
        pass

    def update_total_copies(self):  # update total quantity of books in all lib
        pass

    def update_copies(self):  # update copies quantity of books in one lib
        pass

    def get_book_isbn(self):
        return self.__isbn

    def get_book_title(self):
        return self._title

    def __str__(self):
        return f'Book:\nTitle: {self._title}, Author:{self._author}, ISBN:{self.__isbn}'
