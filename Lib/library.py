from customer import Customer


class Library:

    def __init__(self):
        self._books = []
        self._users = []

    def add_books(self, *args):
        for book in args:
            self._books.append(book)

    @staticmethod
    def delete_books(book_isbn, lib):
        if hasattr(lib, '_books'):

            for items in lib._books:
                for book in items:

                    if book.get_book_isbn() == book_isbn:
                        items.remove(book)

    def register_user(self, *args):  # register user in lib
        usrs = [user for user in args if user not in self._users and isinstance(user, Customer)]
        self._users.extend(usrs)

    def show_users(self):
        for user in self._users:
            print(user)

    @staticmethod
    def find_book(book_isbn, *args):  # find book using ISBN
        for lib in args:

            if hasattr(lib, '_books'):

                for item in lib._books:
                    for book in item:

                        if book.get_book_isbn() == book_isbn:
                            print(book)
                            return book
                else:
                    return f'Book not found'

    def show_available_books(self):  # show all books in lib
        if self._books is not None:
            [print(book) for book_lst in self._books for book in book_lst]
