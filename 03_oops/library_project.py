# Decorator
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


class Book:
    def __init__(self) -> None:
        self.books = [{"id": 1, "name": "Being You - Anil Seth", "available": True}]

    @log_action
    def add_book(self, name: str):
        id = self.books[-1]["id"] + 1
        book = {"id": id, "name": name, "available": True}

        self.books.append(book)

        print("Book added successfully!!!")
        return True

    def borrow_book(self, name: str):
        book = None
        for bookItem in self.books:
            if bookItem["name"] == name:
                book = bookItem
                bookItem["available"] = False

        if book is None:
            return "Failed to borrow book"

        print("Book borrowed successfully!!!!")
        return True

    def available_books(self):
        for book in self.books:
            if book["available"]:
                yield book["name"]

    def borrowed_books(self):
        for book in self.books:
            if not book["available"]:
                print(book["name"])

    def return_book(self, name):
        for book in self.books:
            if book["name"] == name:
                book["available"] = True
                return "Thank You! Book returned successfully!"

        return "Sorry! Book not found!!"


shop = Book()

for book in shop.available_books():
    print(book)

shop.add_book("DDIA")
