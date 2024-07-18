class Book:
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"    
        
book1 = Book("Book: Pride and Prejudice", "Jane Austen")
print (book1)
        # print(f"Book: ", self.title, " by " , self.author) 
        # pass

class EBook(Book):
    def __init__(self, title, author, file_size ):
        super().__init__(title, author)
        self.file_size = file_size
        print(f"EBook: {title} by {author}, File Size: {file_size}KB")
        pass
        
        
class PrintBook(Book):
    def __init__(self, title, author, page_count ):
        super().__init__(title, author)
        self.page_count = page_count
        print(f"PrintBook: {self.title} by {self.author}, Page Count: {page_count}")
        pass
    
    
    
    
    
    
    
class Library():
    # def __init_subclass__(cls) -> None:
    #     return super().__init_subclass__()
    def __init__(self):
         self.books = []
        
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book) 


        # else:
        #     raise TypeError ("Only Book objects can be added to the library") 

        if isinstance(book, EBook):
            self.books.append(book) 


        elif isinstance(book, PrintBook):
            self.books.append(book)      


        else:
            pass


    def list_books(self):
        for book in self.books:
            return book
    
        
# class Library():
#     def __init__(self):
#          self.books = []
           
#     def add_book(self, book):
#         if isinstance(book, Book):
#             self.books.append(book)  
            
            
#     if isinstance(book, EBook):
#             self.books.append(book) 


#         elif isinstance(book, PrintBook):
#             self.books.append(book)                 
     
     


#         # else:
#         #     raise TypeError ("Only Book objects can be added to the library") 

       

        
        

        
        
# library = Library()

# ebook = EBook("1984", "George Orwell",  "PDF")
# printbook = PrintBook("To Kill a Mockingbird", "Harper Lee",  324)

# library.add_book(ebook)
# library.add_book(printbook)

# print("Listing all books in the library:")
# library.list_books()

# print("\nFinding a book by title:")
# book = library.find_book_by_title("1984")
# if book:
#     print(book)
# else:
#     print("Book not found.")

# library.list_books()
        
        
        
        
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     # def __str__(self):
#     #     return f" {self.title,}  by  {self.author} "   


# class EBook(Book):
#     def __init__(self, title, author, file_size):
#         super().__init__(title, author, file_size)
#         self.file_size = file_size


# class PrintBook(Book):
#     def __init__(self, title, author, page_count ):
#         super().__init__(title, author, page_count)
#         self.page_count = page_count   
        
        
        
        
        
# class Library():
#     # def __init_subclass__(cls) -> None:
#     #     return super().__init_subclass__()
#     def __init__(self):
#          self.books = []
        
        
#     def add_book(self, book):
#         if isinstance(book, Book):
#             self.books.append(book) 
               
#         # else:
#         #     raise TypeError ("Only Book objects can be added to the library") 
        
#         if isinstance(book, EBook):
#             self.books.append(book) 
            
            
#         elif isinstance(book, PrintBook):
#             self.books.append(book)      
            
            
#         else:
#             raise TypeError ("Only Book objects can be added to the library") 
             
       
#     def list_books(self):
#         for book in self.books:
#             return book
                     
        
            