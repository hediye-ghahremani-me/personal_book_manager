from books import show_books

name = input("Enter your name : ")
print("Welcome, ", name, "!")

books = []
count = int(input("How many books do you want to add ? "))

for i in range(count):
    book = input("Enter a book name : ")
    books.append(book)

print("Your books :")
show_books(books)