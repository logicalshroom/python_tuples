# Task 1: Add a functionality to add new books

# 1. Request user input
# 2. Create a tuple, assigned to a variable
# 3. Slice the tuple into the list
# 4. error checking for duplicates

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def addbook():
    global library
    title = str(input("Please input the book's title: "))
    author = str(input("Please input the book's author: "))
    book = (title, author)
    if book in library:
        print("Duplicate Detected.")
    else:
        library.append(book)
        print(f"{title} by {author} Successfully Added.")

def printlib():
    print(f"Here's your library!\n{library}")

addbook()

addbook()

printlib()
