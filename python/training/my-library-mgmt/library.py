from books import Book

class Library:

    name = 'ABC Book Store'

    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book_id, book_name, book_price):
        book_obj = Book(book_id, book_name, book_price)
        self.books.append(book_obj)

    def add_book_obj(self, book_obj):
        self.books.append(book_obj)

    def remove_book(self):
        pass

    def add_user(self):
        pass

    def remove_user(self):
        pass

    def get_book_count():
        return Book.total_count

    def __str__(self):
        return f"name: {Library.name} | books: {len(self.books)} | user: {len(self.users)}"


if __name__ == '__main__':
    lib_obj = Library()
    print(lib_obj)

    # Add book to library
    lib_obj.add_book(1, 'maths', 100)
    print(lib_obj)

    book_obj = Book(2, 'physics', 350)
    lib_obj.add_book_obj(book_obj)
    print(lib_obj)

