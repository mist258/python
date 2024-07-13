from manage_lib import ManageLibraries
from base_book import Book
from base_user import User

class Library(ManageLibraries):
    def __init__(self):
        self._users: list[User] = [] # list of all users in lib
        self._books: list = [] # list of all books
        self._borrowed_books: list[Book] = []

    def register_user_in_lib(self, customer: User):
        self.register_user(customer)

    def show_available_books_in_lib(self):
        self.show_available_books()

    def show_users_in_lib1(self):
        self.show_users()

    def give_book_for_customer_lib1(self, customer_id, book_title):
        self.give_book_for_customer(customer_id, book_title)


