import re


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
    def check_availability(book_isbn, *args):  # check whether the book is available in library using ISBN
        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if book_isbn == book.get_book_isbn():
                        print(f'Book \'{book._title}\' is available in libraries')

    @staticmethod
    def update_total_copies(book_isbn, *args):  # update current book copies in all libraries

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
    def update_copies(book_isbn, library):  # updates copies in only one library

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