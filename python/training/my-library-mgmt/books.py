class Book:

    total_count = 0

    def __init__(self, book_id, book_name, book_price, book_quantity=1, book_publisher=None):
        self.id = book_id
        self.name = book_name
        self.price = book_price
        self.publisher = book_publisher
        self.quantity = book_quantity
        Book.total_count += 1

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"id: {self.id} name: {self.name}  quantity:{self.quantity} prices:{self.price} publisher: {self.publisher}"

    def get_book_count(self):
        return Book.total_count

    def __del__(self):
        Book.total_count -= 1

if __name__ == '__main__':
    my_first_book = Book(1, 'maths', 100)
    print(my_first_book)

    my_second_book = Book(2, 'physics', 350)
    print(my_second_book)
    
    book_count = my_first_book.get_book_count()
    # book_count = my_second_book.get_book_count()
    print(f"book count: {book_count}")

    del my_second_book
    book_count = my_first_book.get_book_count()
    print(f"book count : {book_count}")
