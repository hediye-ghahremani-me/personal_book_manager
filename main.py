from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name : ")
print("Welcome, ", name, "!")

admin_mode = input("Do you want to enter admin mode ? yes/no ")
if admin_mode.lower() == "yes" :
    admin_password = input("Enter admin password : ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("Admin mode activated !")
    else:
        print("Wrong password !")

books = load_books()
count = int(input("How many books do you want to add ? "))

for i in range(count):
    book_name = input("Enter a book name : ")
    priority = input("Enter priority : (low / medium / high) ").lower()
    book = {
        "name": book_name,
        "priority": priority
    }
    books.append(book)

print("Your added books:")
show_books(books)
save_books(books)