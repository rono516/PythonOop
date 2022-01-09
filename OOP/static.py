# instance methods work on specific objects
# class methods work on the entire class
# static methods do not modify state of class or object instance
class Book:
    def __init__(self, name, pages, price):
        self.name = name
        self.pages = pages
        self.price = price

    __booklist = None

#double underscore makes this a private variable

#static method to access it
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist    


b1 = Book("Collins", 23, 45)

thebooks = Book.getbooklist()
thebooks.append(b1)
print(thebooks)
