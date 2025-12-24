class Member:
    def __init__(self, name, member_id) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book) -> bool:
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            return True
        return False