from datetime import datetime, timedelta
class Book:
    book_counter = 1000

    def __init__(self, title, author):
        Book.book_counter += 1
        self.book_id = Book.book_counter
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"ID: {self.book_id} | {self.title} | {self.author} | {status}")


# ---------------- USER CLASS ----------------
class User:
    user_counter = 5000

    def __init__(self, name):
        User.user_counter += 1
        self.user_id = User.user_counter
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"User ID: {self.user_id} | Name: {self.name}")


# ---------------- LIBRARY CLASS ----------------
class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.borrow_records = {}

        # Borrowing period
        self.borrow_days = 14

        # ₹5 penalty per late day
        self.penalty_per_day = 5

    # Add a book
    def add_book(self, title, author):
        book = Book(title, author)
        self.books[book.book_id] = book
        print(f"Book added successfully. Book ID: {book.book_id}")

    # Register user
    def add_user(self, name):
        user = User(name)
        self.users[user.user_id] = user
        print(f"User registered successfully. User ID: {user.user_id}")

    # View available books
    def view_available_books(self):
        print("\n------ AVAILABLE BOOKS ------")

        found = False

        for book in self.books.values():
            if book.is_available:
                book.display()
                found = True

        if not found:
            print("No books are currently available.")

    # Borrow book
    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print("Invalid user ID.")
            return

        if book_id not in self.books:
            print("Invalid book ID.")
            return

        book = self.books[book_id]
        user = self.users[user_id]

        if not book.is_available:
            print("Book is already borrowed.")
            return

        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=self.borrow_days)

        book.is_available = False
        user.borrowed_books.append(book_id)

        self.borrow_records[book_id] = {
            "user_id": user_id,
            "borrow_date": borrow_date,
            "due_date": due_date
        }

        print("\nBook borrowed successfully!")
        print(f"Book: {book.title}")
        print(f"Borrow Date: {borrow_date.strftime('%Y-%m-%d')}")
        print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")

    # Return book
    def return_book(self, book_id):
        if book_id not in self.books:
            print("Invalid book ID.")
            return

        if book_id not in self.borrow_records:
            print("This book is not currently borrowed.")
            return

        record = self.borrow_records[book_id]

        user_id = record["user_id"]
        due_date = record["due_date"]
        return_date = datetime.now()

        # Calculate late days
        late_days = max(0, (return_date.date() - due_date.date()).days)

        penalty = late_days * self.penalty_per_day

        # Update book status
        self.books[book_id].is_available = True

        # Remove book from user's borrowed list
        user = self.users[user_id]

        if book_id in user.borrowed_books:
            user.borrowed_books.remove(book_id)

        # Remove borrowing record
        del self.borrow_records[book_id]

        print("\nBook returned successfully!")
        print(f"Return Date: {return_date.strftime('%Y-%m-%d')}")

        if late_days > 0:
            print(f"Late by: {late_days} day(s)")
            print(f"Penalty: ₹{penalty}")
        else:
            print("Returned on time.")
            print("Penalty: ₹0")

    # View borrowed books
    def view_borrowed_books(self, user_id):
        if user_id not in self.users:
            print("Invalid user ID.")
            return

        user = self.users[user_id]

        print(f"\n------ BOOKS BORROWED BY {user.name} ------")

        if not user.borrowed_books:
            print("No books borrowed.")
            return

        for book_id in user.borrowed_books:
            book = self.books[book_id]
            record = self.borrow_records[book_id]

            print(f"Book ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(
                f"Due Date: "
                f"{record['due_date'].strftime('%Y-%m-%d')}"
            )
            print("------------------------")


# ---------------- MAIN PROGRAM ----------------

library = Library()

while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Register User")
    print("3. View Available Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View User's Borrowed Books")
    print("7. View All Users")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        library.add_book(title, author)

    elif choice == "2":
        name = input("Enter user name: ")

        library.add_user(name)

    elif choice == "3":
        library.view_available_books()

    elif choice == "4":
        try:
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))

            library.borrow_book(user_id, book_id)

        except ValueError:
            print("Please enter valid numeric IDs.")

    elif choice == "5":
        try:
            book_id = int(input("Enter Book ID: "))

            library.return_book(book_id)

        except ValueError:
            print("Please enter a valid Book ID.")

    elif choice == "6":
        try:
            user_id = int(input("Enter User ID: "))

            library.view_borrowed_books(user_id)

        except ValueError:
            print("Please enter a valid User ID.")

    elif choice == "7":
        print("\n------ REGISTERED USERS ------")

        if not library.users:
            print("No users registered.")
        else:
            for user in library.users.values():
                user.display()

    elif choice == "8":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
