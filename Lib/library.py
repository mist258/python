from customer import Customer


class Library:

    def __init__(self):
        self._books = []
        self._users = []

    def add_books(self, *args):  # DONE
        for book in args:
            self._books.append(book)

    @staticmethod
    def delete_books(book_isbn, lib):  # DONE
        if hasattr(lib, '_books'):
            for book in lib._books:
                if hasattr(book, 'get_book_isbn') and book.get_book_isbn() == book_isbn:
                    lib._books.remove(book)

    def register_user(self, *args):  # register user in lib DONE
        usrs = [user for user in args if user not in self._users and isinstance(user, Customer)]
        self._users.extend(usrs)

    def show_users(self):  # DONE
        for user in self._users:
            print(user)

    @staticmethod
    def find_book(book_isbn, *args):  # find book using ISBN DONE
        for lib in args:
            if hasattr(lib, '_books'):
                for book in lib._books:
                    if hasattr(book, 'get_book_isbn') and book.get_book_isbn() == book_isbn:
                        print(book)
                        return book
                else:
                    return f'Book not found'

    def show_available_books(self):  # show all books in lib DONE
        if self._books is not None:
            for book in self._books:
                print(book)
