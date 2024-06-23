"""5. Создать класс Library,
который будет управлять книгами.
Каждая книга должна иметь атрибуты title, author и year.
Класс Library должен иметь методы для добавления книги
.add_book(), удаления книги .remove_book() и поиска книги по названию .find_book()"""

class Book:
    def __init__(self, title_pm: str, author_pm: str, year_pm: int):
        self.title = title_pm
        self.author = author_pm
        self.year = year_pm

    def __str__(self):
        return f"'{self.title}' Купил {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print(f"No book found with title: {title}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book found: {book}")
                return book
        print(f"No book found with title: {title}")
        return None

# Примеры использования классов

# Создаем библиотеку
library = Library()

# Создаем книги
book1 = Book("Степной Волк!", "Джордж Клейсон", 1949)
book2 = Book("Самый Богатый Человек в Вавилоне! ", "Роберт Кийосаки", 1960)
book3 = Book("Белый Клык!", "Жек Лондон", 1925)

# Добавляем книги в библиотеку
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Ищем книгу по названию
library.find_book("1984")
library.find_book("Moby Dick")

# Удаляем книгу
library.remove_book("1984")
library.remove_book("Moby Dick")

# Проверяем оставшиеся книги
print("\n Оставшиеся книги в библиотеке:")
for book in library.books:
    print(book)
