from base_book import Book, ManageBooksCopies
from customer import Customer
from library import Library
from employee import Employee


def main():

    # class initialization
    book1: list[Book] = [
        Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7'),
        Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7'),
        Book('Baptism of Fire', 'Andrzej Sapkowski', '978-0-575-08678-0'),
        Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0'),
        Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0'),
        Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0'),
        Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')]

    book2: list[Book] = [
        Book('Sword of Destiny', 'Andrzej Sapkowski', '978-0-316-27805-7'),
        Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7'),
        Book('Blood of Elves', 'Andrzej Sapkowski', '978-0-575-08636-0'),
        Book('Time of Contempt', 'Andrzej Sapkowski', '978-0-575-08637-7')]

    # class initialization
    cust1 = Customer('Anny', 1, 'any.email@gmail.com')
    cust2 = Customer('Mark', 2, 'mark.email@gmail.com')
    cust3 = Customer('Nick', 3, 'nick.email@gmail.com')
    cust4 = Customer('Sam', 4, 'sam.email@gmail.com')

    # class initialization Lib1
    library = Library()
    library.register_user(cust2, cust1) # register user
    # library.show_users()  #show all users in lib1

    # class initialization Lib2
    library2 = Library()
    library2.register_user(cust4, cust3) # register user
    # library2.show_users()  #show all users in lib2


    # class initialization
    empl1 = Employee(1333, 100, library)
    empl1.add_book_to_lst(book1) # add list of book

    empl2 = Employee(1222, 100, library2)
    empl2.add_book_to_lst(book2)  # add list of book

    # print(f'\nLibrary 1')
    # library.show_available_books()
    # show available books in lib
    # print(f'\nLibrary 2')
    # library2.show_available_books()

    # print(empl1.get_salary()) #get salary to employee

    #empl1.delete_book_from_lst('978-0-316-27805-7', library2)
    #library2.show_available_books()
    # deleting books fom library
    # empl2.delete_book_from_lst('978-0-575-08678-0', library)
    # library.show_available_books()

    # print(empl2.finding_books('978-0-575-08637-7', library)) # finding books

    manage_copies = ManageBooksCopies()
    # print(manage_copies.update_total_copies(library2)) # return total quantity of books copies in lib
    # print(manage_copies.update_copies('978-0-575-08637-7', library)) # return quantity only one books copies in lib

    empl1.give_book_to_user('Sword of Destiny', cust1, library, library2) # give book to user
    #cust1.show_borrowed_books() # show borrowed books by user
    empl2.return_book(cust1, '978-0-575-08637-7') # return borrowed books
    cust1.show_borrowed_books()


if __name__ == "__main__":
    main()
