# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)

#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library():
    #creating a book list
    def __init__(self, books_names, library_name):
        self.lend_data = {}
        self.books_names = books_names
        self.library_name = library_name
        
        #adding books to dictionary
        for books in self.books_names:
            self.lend_data[books] = None

    #displaying the book
    def display_book(self):
        for index, books in enumerate(self.books_names):
            print(f"{index} - {books}")

    #lending the book
    def lend_book(self, book, lender):
        if book in self.books_names:
            if self.lend_data is None:
                self.lend_data = lender
                print("Book lended Succesfully!")
            else: print(f"Sorry, This book is already lend by {self.lend_data[book]}")
        else: print("You entered wrong book name.")

    #adding the book
    def add_book(self, book):
        self.books_names.append(book)
        self.lend_data[book] = None
    
    #deleting the book
    def delete_book(self, book):
        self.books_names.pop(book)
        self.lend_data.pop(book)

    #returning the book
    def return_book(self, book):
        if book in self.books_names:
            if book in self.books_names is not None:
                self.books_names.pop(book)
            else: print("Sorry, This Book is not lend Yet")
        else: print("Sorry, You Entered Wrong Book Name.")
        
        
def main():
    #default variables
    list_of_books = ["Woven for love", "Half girlfriend", "13 reasons why", "2 state", "Bytes of python"]
    library_name = "saurav"
    password = 123345
    
    saurav = Library(list_of_books, library_name)
    
    print(f"----------WELCOME TO THE {(library_name.upper())} LIBRARY----------")
    print("Press 'd' to display the books\n Press 'l' to lend the book\n Press 'a' to add the book\n Enter 'del' to delete the book\n Press 'r' to return the book\n Enter 'exit' to step out of library")
    Exit = False
    while(Exit is not True):
        user_input = input("What do you want to do: ")
        
        if user_input == "exit":
            Exit is True
        
        if user_input == "d":
            saurav.display_book()
            
        if user_input == "l":
            input1 = input("What is your name: ")
            input2 = input("Which book you want to lend: ")
            saurav.lend_book(input2, input1)
            
        if user_input == "a":
            input1 = input("What is the name for your book?: ")
            print("Book Added Succsesfully!")
            saurav.add_book(input1)
        
        if user_input == "del":
            input1 = input("Which book you want to delete?: ")
            input2 = input("Enter password to proceed: ")
            if input2 == 12345:
                print("Book Deleted Succesfully!")
                saurav.delete_book(input1)
            
        if user_input == "r":
            user1 = input("Which book you want to return: ")
            saurav.return_book(user1)
            

main()
        
            
        