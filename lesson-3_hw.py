#####################################
"""
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін
  """


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()


rec1 = Rectangle(3, 4)
rec2 = Rectangle(5, 6)
print(rec1 + rec2)
#########################################

"""
створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        self.count_inc()

    @classmethod
    def count_inc(cls):
        cls.count += 1

    def __str__(self):
        return f'{self.name} is {self.age} years old with {self.foot_size} foot '

    def __repr__(self):
        return self.__str__()


class Prince(Human):
    cinderella_list = []

    def __init__(self, name, age, cinderella_foot_size):
        super().__init__(name, age)
        self.cinderella_foot_size = cinderella_foot_size

    def add_and_find_cinderella(self, item):
        if isinstance(item, Cinderella):
            self.cinderella_list.append(item)
            if item.foot_size == self.cinderella_foot_size:
                print(f'Cinderella {item} found at {self.cinderella_foot_size} ')


c1 = Cinderella('A', 20, 10)
c2 = Cinderella('B', 18, 5)
c3 = Cinderella('C', 16, 8)
print(Cinderella.count)

p1 = Prince('Pr1', 25, 5)
p1.add_cinderella(c1)
p1.add_cinderella(c2)
p1.add_cinderella(c3)


##################################################

"""
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
"""

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()



class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Main:
    printable_list = []

    def add(self, item):
        if isinstance(item, Book) or isinstance(item, Magazine):
            self.printable_list.append(item)

    def show_all_magazines(self):
        all_magazines = [magazin for magazin in self.printable_list if isinstance(magazin, Magazine)]
        print(all_magazines)

    def show_all_books(self):
        all_books = [book for book in self.printable_list if isinstance(book, Book)]
        print(all_books)


book1 = Book('Book1')
book2 = Book('Book2')
magazine1 = Magazine('Magazine1')
magazine2 = Magazine('Magazine2')

main = Main()
main.add(book1)
main.add(book2)
main.add(magazine1)
main.add(magazine2)
main.show_all_magazines()
main.show_all_books()







