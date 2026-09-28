from book import Book

def menu_options():
    """Creates a menu that the user can choose from"""
    print("1. Add a new book")
    print("2. List all books")
    print("3. Find a book")
    print("4. Exit the program")

def add_book(library):
    """Adds a new book to the library"""
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    isbn = input("Enter the ISBN: ")

    # Create an object that holds information entered by user
    user_book = Book(title, author, isbn)
    library.append(user_book)

def list_books(library):
    """Lists all books in the library"""
    for book in library:
        print(book)

def find_book(library,query):
    """Finds a book from the library"""
    query = query.lower()

    for book in library:
        if query in book.title.lower() or query in book.author.lower():
            return book

    return None

# Create an empty list to store books
my_library = []

# Starts the program asking user to choose an option
while True:
    menu_options()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book(my_library)
    elif choice == "2":
        list_books(my_library)
    elif choice == "3":
        search = input("Enter the title or author of the book that you want to find: ")
        found_book = find_book(my_library, search)

        if found_book:
            print(found_book)
        else:
            print("The book you are looking for is not available!")

    elif choice == "4":
        print("Thank you for using this program!")
        break
    else:
        print("Please try again!")
