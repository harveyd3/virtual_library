class Book:
    def __init__(self, title, author, isbn):
        """Stores the title, author, and ISBN of the book"""
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Formats book info into a string"""
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

    def get_details(self):
        """Returns the book details as a dictionary"""
        book_details = {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }
        return book_details
