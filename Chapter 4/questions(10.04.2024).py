books = []

def Qadd(books):
    number_of_books = int(input("Enter number of books: "))
    for i in range(number_of_books):
        name = input("Name: ")
        books.append(name)
        


def Qdel(books):
    print(books)
    number_of_books_delete = int(input("Enter number of books to delete: "))
    for j in range(number_of_books_delete):
        name_to_delete = input("Enter name: ")
        print(name_to_delete)
        books.pop(2)
        print("Item deleted")


    print("Updated list: ", books)

def disp(books):
    print(books)

#Calling all functions

Qadd(books)
Qdel(books)
disp(books)

