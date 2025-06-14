class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"

my_book = Book("1984", "Джордж Видер", 1939)
print(my_book.info())