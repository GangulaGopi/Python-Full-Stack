class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1
    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)
b1 = Book("AI", "John")
b2 = Book("Python", "Guidovanrussen")
b3 = Book.from_string("send-gopi")
print(b1.title,"-",b1.author)
print(b2.title,"-",b2.author)
print(b3.title ,"-" ,b3.author)
print(Book.total_books)


