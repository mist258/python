from library import Library
from customer import Customer


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

    def add_book_to_lst(self, *args):  # add book to lib
        return self.collection.add_books(*args)

    def delete_book_from_lst(self, book_isbn, lib):  # delete book from lib using ISBN
        return self.collection.delete_books(book_isbn, lib)

    def finding_books(self, book_isbn, *args):  #
        return self.collection.find_book(book_isbn, *args)

    @staticmethod
    def give_book_to_user(book_title, customer: Customer, *args):  # give book to user DONE
        book_list = [book for lib in args if hasattr(lib, "_books") for sub_list in lib._books for book in sub_list] # return list all books in libs
        for book in book_list:
            if book.get_book_title() == book_title:
                customer._borrowed_books.append(book)
                book_list.remove(book)
        print(book_list)

    def return_book(self, customer: Customer, book_isbn):  # return book from user
        returned_book_list =[]
        for book in customer._borrowed_books:
            if book.get_book_title() == book_isbn:
                returned_book_list.append(book)
                customer._borrowed_books.remove(book)
