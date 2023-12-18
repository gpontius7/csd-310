# Title: whatabook.py
# Author: Gregory Pontius
# Date: December 17, 2023

import sys
import mysql_connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("Main Menu")
    print("1. View Locations \n 2. View Books In Stock \n 3. User Account \n 4. Exit")

    try:
        choice = init(input('Enter an option:'))
        return choice
    except ValueError:
        print("That choice is not an option")
        sys.exit(0)

def show_locations(_cursor):        
    _cursor.execute("SELECT store_id, locale FROM store")

    locations = _cursor.fetchall()

    print("Stores")

    for location in locations:
        print("Locale: {}\n".format(location[1]))

def show_books(_cursor):
    _cursor.execute ("SELECT book_id, book_name, author, details FROM book")

    books = _cursor.fetchall()

    print("Books")
    for book in books:
        print("Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))

def validate_user():
    try:
        user_id = int(input('Enter user ID:'))

        if user_id < 0 or user_id > 3:
            print("Invalid user")
            sys.exit(0)

        return user_id
    
    except ValueError:
        print("Invalid user")

        sys.exit(0)

def show_account_menu():
    try:
        user_id = int(input('Enter user ID'))

        if user_id < 0 or user_id > 3:
            print("Invalid User ID")
            sys.exit(0)

            return user_id
        
    except ValueError:
        print("Invalid option")

        sys.exit(0)

def show_account_menu():
    try:
        print("Customer Menu")
        print("1. View Wishlist \n 2. Add Book to Wishlist \n 3. Return to the Main Menu")
        account_option = int(input('Choose an option'))
        return account_option
    
    except ValueError:
        print("Invalid option")
        sys.exit(0)

def show_wishlist(_cursor, user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + "FROM wishlist " + "INNER JOIN user ON wishlist.user_id = user.user_id " + "INNER JOIN book ON wishlist.book_id = book.book_id " + "WHERE user.user=id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("-Wishlist-")

    for book in wishlist:
        print("Book Name:{}\n Author:{}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details  FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("- Available Books -")

    for book in books_to_add:
        print("Book ID: {}\n Book Name:{}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUE({}, {})".format(_user_id, _book_id))

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("Welcome")

    user_selection = show_menu

    while user_selection != 4:

        if user_selection == 1:
            show_locations(cursor)

        if user_selection == 2:
            show_books(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                    
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    book_id = int(input("Enter the id of the book you want to add:"))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit()
                    print("Book ID: {} was added to your wishlist."format(book_id))

                if account_option < 0 or account_option > 3:
                        print("That was not a valid ID")
                        account_option = show_account_menu()

                if user_selection < 0 or user_selection > 4:
                    print("That was not option")

                    user_selection = show_menu()
except mysql.connector.Error as err:                    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("One of the supplied credentials is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Databaser does not exist")

    else:
        print(err)

finally:
    db.close()

