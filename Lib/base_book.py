import re


class Book:

    __slots__ = ('_title', '_author', '__isbn', 'copies', 'total_copies')

    def __init__(self, title, author, isbn):
        self.valid_isbn(isbn)

        self._title = title
        self._author = author
        self.__isbn = isbn
        self.copies = None  # books copies in one library

    @classmethod
    def valid_isbn(cls, isbn: str):  # checks for ISBN validity
        pattern_isbn = r'^(?:\d{3})-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,7})-(?:\d{1})$'  # since 2007 ISBN contains 13 digits
        if not re.fullmatch(pattern_isbn, isbn):
            raise ValueError('Invalid ISBN number')

    def get_book_isbn(self):
        return self.__isbn

    def get_book_title(self):
        return self._title

    def __str__(self):
        return f'Book:Title: {self._title}, Author:{self._author}, ISBN:{self.__isbn}'


class ManageBooksCopies:
    def __init__(self):
        self.total_copies = None
        self.copies = None

    def update_total_copies(self, *args):  # update total quantity of books in all lib DONE
        self.total_copies = {}

        for lib in args:
            for item in lib._books:
                for book in item:
                    book = str(book)

                    if book in self.total_copies:
                        self.total_copies[book] += 1
                    else:
                        self.total_copies[book] = 1

        return self.total_copies

    def update_copies(self, book_isbn, lib):  # update copies quantity of books in one lib
        self.copies = {}

        for item in lib._books:
            for book in item:
                # book = str(book)

                if book_isbn == book.get_book_isbn():
                    self.copies[book] += 1




