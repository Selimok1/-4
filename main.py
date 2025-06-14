class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"
class EBook(Book):
    def info(self):
        return f"EBook: {self.title}, {self.author}, {self.year}"

my_book = Book("1984", "Джордж Оруэлл", 1949)
my_ebook = EBook("1984", "Джордж Оруэлл", 1949)

print(my_book.info())
print(my_ebook.info())
