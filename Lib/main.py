from Lib import *

def main():
    # class initialization
    book1 = Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7')
    book2 = Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')
    book3 = Book('Baptism of Fire', 'Andrzej Sapkowski', '978-0-575-08678-0')
    book4 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
    book5 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
    book6 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
    book7 = Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')

    # class initialization
    cust1 = Customer('Anny', 1, 'any.email@gmail.com')
    cust2 = Customer('Mark', 2, 'mark.email@gmail.com')
    cust3 = Customer('Nick', 3, 'nick.email@gmail.com')
    cust4 = Customer('Sam', 4, 'sam.email@gmail.com')

    # class initialization
    lib1 = Library()
    lib1.register_user(cust1) # add user to lib1
    lib1.register_user(cust2)

    # class initialization
    lib2 = Library2()
    lib2.register_user(cust3) # add user to lib1
    lib2.register_user(cust4)

    # show users in libraries
    # print(lib1.show_users_in_lib1())
    # print(lib2.show_users_in_lib2())

    # class initialization
    empl = Employee(1200, 100)
    #print(empl.get_salary()) # get salary to employee

    # add book in both libraries or one
    empl.add_book(book1, lib1, lib2)
    empl.add_book(book2, lib1, lib2)
    empl.add_book(book3, lib1, lib2)
    empl.add_book(book4, lib1)
    empl.add_book(book5, lib1)
    empl.add_book(book6, lib1)
    empl.add_book(book7, lib1)

    # delete book from lib
    #empl.delete_book('978-0-575-08637-7', lib1, lib2)

    # find book (check availability) in libraries
    #empl.find_book(book1.get_book_isbn(), lib1, lib2)
    #empl.find_book(book6.get_book_isbn(), lib1, lib2)

    # show available books in lib
    # print(lib1.show_available_books_in_lib())
    # print(lib2.show_available_books_in_lib2())

    # give book for customer
    lib1.give_book_for_customer_lib1(1, 'Sword of Destiny')
    lib2.give_book_for_customer_lib2(3, 'Time of Contempt')

    # show borrowed_books by customer
    #print(cust1.show_borrowed_books())
    #print(cust3.show_borrowed_books())

    # delete book by customer
    #cust1.delete_book('Sword of Destiny')
    #print(cust1.show_borrowed_books())
    #cust1.return_book(lib2) # return book

    # show current number of books copies in both libraries or one lib (use books ISBN)
    #print(Book.update_total_copies(book7.get_book_isbn(),  lib1))
    #print(Book.update_total_copies(book7.get_book_isbn(),  lib1, lib2))


if __name__ == "__main__":
    main()
