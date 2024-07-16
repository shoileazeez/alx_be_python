class Book:
    def __init__(self, title, author , year )  -> str:
        self.title = title
        self.author = author
        self.year = year
        pass
        
    def __del__(self):
        print("deleting " + self.title)   
          
    def __str__(self) -> str:
        return  f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self) -> str:
        return f"Book('{self.title}', go'{self.author}', {self.year})"
        
       