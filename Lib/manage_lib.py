from base_user import User


class ManageLibraries:
    def register_user(self, customer: User): # registration users in library
        if hasattr(self, '_users'):
            if not isinstance(customer, User):
                raise TypeError('Customer must be of type User')
            elif customer not in self._users:
                self._users.append(customer)
            else:
                raise ValueError('Customer already registered')

    def show_available_books(self,):  # show available books in all libraries
        if hasattr(self, '_books'):
            if self._books is not None:
                for book in self._books:
                    print(book)
            else:
                print('No books available')

    def show_users(self):  # show all users
        if hasattr(self, '_users'):
            if self._users is not None:
                for user in self._users:
                    print(user)
            else:
                print('Field USERS is empty')

    def give_book_for_customer(self, customer_id: User, book_title): # give book for customer from library

        found_cust = None
        found_book = None

        if hasattr(self, '_users'):
            for user in self._users:
                if hasattr(user, '_user_id'):
                    if user._user_id == customer_id:
                        found_cust = user
                    break
        if found_cust is None:
            raise ValueError('Customer not registered')

        if hasattr(self, '_books'):
            for book in self._books:
                if hasattr(book, '_title') and book._title == book_title:
                    found_book = book
                    break

        if found_book is None:
            raise ValueError('Book does not in library')

        found_cust._borrowed_books.append(found_book)
