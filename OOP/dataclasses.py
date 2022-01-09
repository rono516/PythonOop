from dataclasses import dataclass, field

@dataclass
class Book:
    #default values
    title: str = "No Title"
    author: str = "Rono"
    pages: int = 4
    price: float = field(default = 10.0)

    # _str_
    def bookinfo(self):
        return "{self.title}, by {self.author}"

bw = Book("Py101", "Michael Drowell", 67, 10.01)    
print(bw.title, bw.author, sep='')