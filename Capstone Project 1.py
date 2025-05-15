listBooks = []
cart = []

def mainMenu():
    print(f''' 
    --Welcome to the Library system!--
    Please choose what you want to do:
    1. Show list of Books
    2. Search Books
    3. Add a new Book log
    4. Delete an Existing Book log
    5. Borrow a Book
    6. Return a Book
    7. Edit a Book tag
    8. Recommend a Book
    9. Exit''')

def addBook():
    newBook = input("Name of the Book: ")
    newAuthor = input("Name of the Author: ")
    pubYear = input("Publishing Year: ")
    copy = int(input("No. of Copies Available: "))
    newTag = input("Tag (comma separated): ").split(',')
    initials = "".join(map(lambda word: word[0].upper(), newAuthor.split()))
    bookID = initials + str(pubYear) + str(len(listBooks)+1)
    newBuku = {
        "Book ID": bookID,
        "Book Name": newBook,
        "Author": newAuthor,
        "Publishing Year": pubYear,
        "No. of Copies": copy,
        "Tag": [tag.strip().lower() for tag in newTag]
    }
    listBooks.append(newBuku)
    print(f"Book '{newBook}' successfully added.")

def showBooks():
    print("Book Directory:")
    print(f"{'ID':<10} | {'Book Name':<25} | {'Author':<20} | {'Publishing Year':<15} | {'Copies':<8} | {'Tag'}")
    print("-" * 100)
    for books in listBooks:
        print(f"{books['Book ID']:<10} | {books['Book Name']:<25} | {books['Author']:<20} | {books['Publishing Year']:<15} | {books['No. of Copies']:<8} | {', '.join(books['Tag'])}")

def searchBook():
    search = input("What book are you looking for? ").strip().lower()
    found = False
    for x in listBooks:
        if search in x["Book Name"].lower():
            print("Book Found:")
            print(f"{'ID':<10} | {'Book Name':<25} | {'Author':<20} | {'Publishing Year':<15} | {'Copies':<8} | {'Tag'}")
            print("-" * 100)
            print(f"{x['Book ID']:<10} | {x['Book Name']:<25} | {x['Author']:<20} | {x['Publishing Year']:<15} | {x['No. of Copies']:<8} | {', '.join(x['Tag'])}")
            found = True
            break
    if not found:
        print("Book not found, try again.")

def delBook():
    delTitle = input("Name of the book that you want to delete: ").lower()
    for book in listBooks:
        if book['Book Name'].lower() == delTitle:
            listBooks.remove(book)
            print(f"Book '{delTitle}' successfully deleted.")
            return
    print("Book not found.")

def borrowBook():
    while True:
        nameBorBook = input("Name of the book you want to borrow: ").strip().lower()
        JumBorBook = int(input("How many are you borrowing? "))
        for book in listBooks:
            if book['Book Name'].lower() == nameBorBook:
                if JumBorBook > book['No. of Copies']:
                    print(f"There are only {book['No. of Copies']} copies left.")
                else:
                    book['No. of Copies'] -= JumBorBook
                    cartItem = {
                        'Book Name': book['Book Name'],
                        'Copies borrowed': JumBorBook,
                    }
                    cart.append(cartItem)
                    print(f"You have successfully borrowed {JumBorBook} copies of {book['Book Name']}.")
                break 
        else:
            print("Book not found.") 
        again = input("Do you want to borrow another book? (Yes/No): ").strip().lower()
        if again != "yes":
            break

def returnBook():
    while True:
        nameRetBook = input("Name of the book you want to return: ").lower()
        JumRetBook = int(input("How many copies are you returning? "))
        for book in listBooks:
            if book['Book Name'].lower() == nameRetBook:
                book['No. of Copies'] += JumRetBook
                print(f"You returned {JumRetBook} copies of {book['Book Name']}.")
                break
        else:
            print("Book not found.")
        again = input("Do you want to return another book? (Yes/No): ").strip().lower()
        if again != "yes":
            break

def editTag():
    remorad = input("Do you want to add or remove a tag? (add/remove): ").strip().lower()
    name = input("Enter book name: ").strip().lower()
    for book in listBooks:
        if book['Book Name'].lower() == name:
            if remorad == 'add':
                newTags = input("Enter new tag(s) to add (comma separated): ").split(',')
                for tag in newTags:
                    addtag = tag.strip().lower()
                    if addtag not in book['Tag']:
                        book['Tag'].append(addtag)
                print("Tags added.")
            elif remorad == 'remove':
                removeTags = input("Enter tag(s) to remove (comma separated): ").split(',')
                for tag in removeTags:
                    remtag = tag.strip().lower()
                    if remtag in book['Tag']:
                        book['Tag'].remove(remtag)
                print("Tags removed.")
            else:
                print("Please only choose 'add' or 'remove'.")
            return
        print("Book not found.") 

def recommendBook():
    tag = input("What tag are you looking for? ").strip().lower()
    recommended = list(filter(lambda book: tag in book['Tag'], listBooks))
    if recommended:
        print("Books matching your interest:")
        for book in recommended:
            status = "Available" if book['No. of Copies'] > 0 else "Unavailable"
            print(f"{book['Book ID']} | {book['Book Name']} ({status})")
    else:
        print("No recommendations found.")

while True:
    mainMenu()
    menuinput = input("Choose an option (1-9): ")
    if menuinput == "1":
        showBooks()
    elif menuinput == "2":
        searchBook()
    elif menuinput == "3":
        addBook()
    elif menuinput == "4":
        delBook()
    elif menuinput == "5":
        borrowBook()
    elif menuinput == "6":
        returnBook()
    elif menuinput == "7":
        editTag()
    elif menuinput == "8":
        recommendBook()
    elif menuinput == "9":
        print("Thank you for using the Library System!")
        break
    else:
        print("Please input an option from 1 to 9.")
