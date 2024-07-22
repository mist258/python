
from library import Library


class Salary:
    def __init__(self, payment):
        self.valid_payment(payment)

        self.payment = payment

    @classmethod
    def valid_payment(cls, payment):
        if not isinstance(payment, (int, float)):
            raise TypeError('Payment must be of type int or float')

    def get_pay_for_year(self):
        return self.payment * 12


class Employee(Salary):

    def __init__(self, payment, bonus, collection: Library):
        super().__init__(payment)
        self.valid_bonus(bonus)

        self.books_from_customer = []  # get books returned by customers
        self._salary = Salary(payment)
        self._bonus = bonus
        self.collection = collection

    @classmethod
    def valid_bonus(cls, bonus):
        if not isinstance(bonus, (int, float)):
            raise TypeError('Bonus must be of type int or float')

    def get_salary(self):
        return self._salary.get_pay_for_year() + self._bonus

    def add_book_to_lst(self, *args):  # add book to lib DONE
        return self.collection.add_books(*args)

    def delete_book_from_lst(self, book_isbn, lib):  # delete book from lib using ISBN DONE
        return self.collection.delete_books(book_isbn, lib)

    def finding_books(self, book_isbn, *args):  # DONE
        return self.collection.find_book(book_isbn, *args)

    def give_book_to_user(self, user):  # give book to user
        pass

    def return_book(self, book):  # return book from user
        pass
