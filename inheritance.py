#base class
class Publication:
    def __init__(self, title, price):
        self.title= title
        self.price= price

class Periodical(Publication):
    def __init__(self, title, publisher, price, period) :
        super().__init__(title, price)
        self.publisher= publisher
        self.period= period

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__( title, price)
        self.author= author
        self.pages=pages

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

news1 = Newspaper("Nation", "REG", 50, "week")      
print(news1.title)
print (news1.publisher)
print (news1.price)
print( news1.period)
  
