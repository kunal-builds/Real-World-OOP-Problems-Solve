
class Library:
    def __init__(self, name , author, price):
        self.books = []
        self.name = name
        self.author = author
        self.price = price

    def add_book(self, name):
        self.books.append(name)
        print(f"book {name} ADD succesFully")

    def remove(self, name):
        if name in self.books:
            self.books.remove(name)
            print(f"Book {name} Remove SuccesFully")
        else:
            print("not Found")

    def search(self, name):
        if name in self.books:
            print(f"Book {name} Found")

        else:
            print(f"Book {name} Not Found")

lib = Library("Harry", "Autor", 200)
lib.add_book("harru")
lib.remove("haru")
lib.search("haru")












































# Books = [
#     "Theworld","khalu", "345",
#     "Theworld","khalu", "345",
#     "Theworld","khalu", "345",
#     "Theworld","khalu", "345",
#     "Theworld","khalu", "345",
# ]
# class Library:
#     def __init__(self, Bookname, Author, price):
#         self.bookname = Bookname
#         self.Author = Author
#         self.price = price

# while True:
#     print("1. Add_book")
#     print("2. Remove Book")
#     print("3. Search Book")

#     choice = int(input("Enter Your choice: "))

#     if choice == 1:
#         book_name = input("Enter Book name: ")
#         Books.append(book_name)
#         print(f"Book {book_name} added succussfully")

#     elif choice == 2:
#         book_name = input("Enter Book Name: ")
#         if book_name in Books:
#             Books.remove(book_name)
#             print(f"book {book_name} Removed Successfully")
#         else:
#             print("Book Not Found")

#     elif choice == 3:
#         book_name = input("Search Book: ")
#         if book_name in Books:
#             print(f"Book {book_name} is avaible")
#         else:
#             print(f"Book {book_name} Not Found")
        





