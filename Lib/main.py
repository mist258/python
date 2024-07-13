from Lib import *

def main():

    book1 = Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7')
    book2 = Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')
    book3 = Book('Baptism of Fire', 'Andrzej Sapkowski', '978-0-575-08678-0')
    book4 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
    book5 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
    book6 = Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0')
    book7 = Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')

    cust1 = Customer('Anny', 1, 'any.email@gmail.com')
    cust2 = Customer('Mark', 2, 'mark.email@gmail.com')
    cust3 = Customer('Nick', 3, 'nick.email@gmail.com')
    cust4 = Customer('Sam', 4, 'sam.email@gmail.com')

    lib1 = Library()
    lib1.register_user(cust1)
    lib1.register_user(cust2)

    lib2 = Library2()
    lib2.register_user(cust3)
    lib2.register_user(cust4)

    # print(lib1.show_users_in_lib1())
    # print(lib2.show_users_in_lib2())

    empl = Employee(1200, 100)
    #print(empl.get_salary())

    empl.add_book(book1, lib1, lib2)
    empl.add_book(book2, lib1, lib2)
    empl.add_book(book3, lib1, lib2)
    empl.add_book(book4, lib1)
    empl.add_book(book5, lib1)
    empl.add_book(book6, lib1)
    empl.add_book(book7, lib1)

    #empl.delete_book('978-0-575-08637-7', lib1, lib2)

    #empl.find_book(book1.get_book_isbn(), lib1, lib2)
    #empl.find_book(book6.get_book_isbn(), lib1, lib2)

    # print(lib1.show_available_books_in_lib())
    # print(lib2.show_available_books_in_lib2())

    lib1.give_book_for_customer_lib1(1, 'Sword of Destiny')
    lib2.give_book_for_customer_lib2(3, 'Time of Contempt')

    #print(cust1.show_borrowed_books())
    #print(cust3.show_borrowed_books())

    #cust1.delete_book('Sword of Destiny')
    #print(cust1.show_borrowed_books())
    #cust1.return_book(lib2)

    #print(Book.update_total_copies(book7.get_book_isbn(),  lib1))
    #print(Book.update_total_copies(book7.get_book_isbn(),  lib1, lib2))


if __name__ == "__main__":
    main()
