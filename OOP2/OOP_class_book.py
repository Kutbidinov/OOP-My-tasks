class Book:
    def __init__(self,names_pm, author_pm, pages_pm,yearswriting_pm, contents_pm,):
        self.names = names_pm
        self.author = author_pm
        self.pages = pages_pm
        self.yearswriting = yearswriting_pm
        self.contents = contents_pm

    def notification(self):
        print(self.names, self.author, self.pages, self.yearswriting, self.contents)


Book1 = Book(names_pm="NAME =  The Book thief", author_pm="Marcuz Suzak", pages_pm=5343, yearswriting_pm= "This Book writing of 2005 years",
             contents_pm="История о немецкой девочке по имени Лизель")

print(Book1.names)

Bokok2 = Book(names_pm="NAME =  От Нуля к единице", author_pm="Piter Till", pages_pm=182, yearswriting_pm="16 - September, 2014 - yers",
              contents_pm="A future Progress")
print(Bokok2.names)

Book3 = Book(names_pm="NAME =  Сымый Богатый Человек в Вавилоне", author_pm=" George Kleison", pages_pm=181,
             yearswriting_pm=1920, contents_pm="Achieve financial independence")
print(Book3.names)

Book4 =Book(names_pm="NAME = 'Prince of the Siberian Kyrgyz'", author_pm="'В.И. Козодой'", pages_pm=185, yearswriting_pm= "Novosibirsk, 23 - November!",
            contents_pm="История Сибирских Кыргызов!")
print(Book4.names)