class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"{self.title} by {self.author} ({self.year})"

book = Book("Капитанская дочка", "Александр Пушкин", 1836)
print(book.get_info())