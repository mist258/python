from base_user import User


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
