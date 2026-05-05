class Book:
    
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.__pages= pages
        

    def summary(self):
        print(f"{self.title} by {self.author},{self.__pages} pages")

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    @property
    def pages(self):
        return self.__pages
    

class EBook(Book):
    total_ebooks = 0
    def __init__(self,title,author,pages,file_size):
        super().__init__(title,author,pages)
        self.file_size = file_size
        EBook.total_ebooks += 1

    def summary(self):
        super().summary()
        print(f"|File size: {self.file_size} MB")
    


b = Book("Atomic Habits", "James Clear", 320)
print(b)
print(b.pages)
b.summary()

e = EBook("Deep Work", "Cal Newport", 280, 5)
print(e)
e.summary()
print(EBook.total_ebooks)  
    
