
from base_user import User


class Customer(User):

    def __init__(self, _name, _user_id, _user_email):
        super().__init__(_name, _user_id, _user_email)
        self._borrowed_books = []

    def show_borrowed_books(self):
        pass

    def __str__(self):
        return f'Customer:\nName: {self._name}, user_email: {self._user_email}, user_ID: {self._user_id}'
