class Library:
    """Manages the library's books and members"""

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")


    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_available_books(self):
        print(f"\nAvailable books at {self.name}:")
        for book in self.books:
            if book.is_available:
                print(f"  - {book}")

    def display_all_members(self):
        print(f"\nMembers of {self.name}:")
        for member in self.members:
            print(f"  - {member}")

