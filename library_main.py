class Book:
    book_counter=100

    def __init__(self, title, auther):
        Book.book_counter+=1
        self.book_id=Book.book_counter
        self.title=title
        self.auther=auther
        self.availebal=True

    def display(self):
        status="availabel" if self.availebal else "Borrowed"
        print(f"ID {self.book_id} | {self.title} | {self.auther} | {status}")


class User:
    user_counter=200
    def __init__(self, name):
        User.user_counter+=1
        self.user_id=User.user_counter
        self.name=name
        self.borrowed_book=[]

    def display(self):
        print(f"ID {self.user_id} | {self.name} ")



class Librari:
    def __init__(self):

        self.book={}
        self.user={}

        self.borrow_day=0
        self.penailty_per_day=00

    def add_book(self,title,auther):
        book=Book(title,auther)
        self.book[book.book_id]=book
        print(f"Book add success fully ID is {book.book_id}")

    def add_user(self,name):
        user=User(name)
        self.user[user.user_id]=user
        print(f"User add sucess fully ID is: {user.user_id}")

    def view_availebal_books(self):
        print("-------avavilebal books---------")

        found= False

        for book in self.book.values():
            if book.is_availebal:
                self.book()

                found=True

        if not found:
            print("book is not corrently availebal !")

    def borrow_book(self, book_id ,user_id):
        if user_id not in self.user:
            print("ivalid use Id ")
            return
        if book_id not in self.book:
            print("invalid book ID")

        book=self.book[book_id]
        user=self.user[user_id]

        if not book.is_availebal:
            print("book is alrady Borrow ")
            return

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

librari=Librari()

while True:
    print("----------------welcome librari------------------")
    print("1.add_book " )
    print("2.register user ")
    print("3.view availebal book")
    print("4.borrow book") 
    print("5.view all user") 
    print("6.exit")

    choice =int(input("ebter your choice"))

    if choice==1:
        titel=input("Enter book title")
        auther=input("Auther name ")
        librari.add_book(titel,auther)
    elif choice==2:
        name=input("enter rgistr user name ")
        librari.add_user(name)

    elif choice==3:
        librari.view_availebal_books()
    elif choice==4:
        librari.borrow_book()
    elif choice==5:
        print("Register users ")

        if not librari.user:
            print("no user register")
        else:
            for user in librari.user.values():
                user.disply()
    elif choice==6:
        print("thank you !")
        break
    else:
        print("invalid choice")