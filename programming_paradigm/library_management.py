class Book:
    def __init__(self, title, author,__is_checked_out):
        self.author = author
        self.title = title
        self.checked_out = __is_checked_out
        
        
        
        
class Library:
    def __init__(self):
        self.books = []
    
             
    def add_book(self, book):
        self.books.append(book)
        
    def  check_out_book(self, tile):
        for book in self.books:
            if book.title == tile and book.is_avaliable():
                book.check_out()
                print(f"checked out{tile}: ")
                
            else: 
                print(f"book {book} has been checked out or is not in the libary ")  
                
                
                
    def  return_book(self):
         for book in self.books:
             if book.title == book and not book.is_avaliable():
                 return True
             else:
                 print(f"book{book} not borrowed from libery ")
                 
                 
                 
    def list_available_books(self):
        for book in self.books:
            print("*" + book)
        
                     
                 
                            
                
                
         
        
             
             
             

        
        
    