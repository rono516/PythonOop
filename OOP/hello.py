class Book:

    #Properties defined at class level that are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype

    #class method to get booktypes works on class //cls instance not object instance
    @classmethod
    def getbooktypes(cls):    
        return cls.BOOK_TYPES        
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price *self._discount )
        else:
         return self.price    
    def setdiscount(self, amount):
        self._discount = amount
    def setTitle(self, newtitle) :

        self.title = newtitle       
class Newspaper:   
    def __init__(self, name, pages) :
        self.name= name
        self.pages= pages

b1 = Book("Bett", "Rich", 4, 560, "EBOOK")        
b2 = Book("Collo", "Rono", 4, 50, "HARDCOVER")
# print(b2.getPrice())
# b2.setdiscount(0.25)
# print(b2.getPrice())

# print(type(b1) == type(b2))
# print(isinstance (b2, Book) )
# print(isinstance(b1, Newspaper))
# print(isinstance(b2, object))
# //access class attribute

print("Book types: ", Book.getbooktypes())