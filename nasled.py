# 1 задание
"""
from abc import ABC, abstractclassmethod
class Animal():
    def __init__(self,color,name,age):
        self.color = color 
        self.name = name 
        self.age = age 

class MyAbstractClass(ABC):
    @abstractclassmethod
    def say(self):
     pass

class Cat(Animal,MyAbstractClass):
    def say(self):
        print("Meow!")

class Dog(Animal, MyAbstractClass):
    def say(self):
        print("Woof!")

cat = Cat("White","Mursik",3)
cat.say()
"""
# 2 задание 
"""
class Father:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname

class Child(Father):
    def __init__(self, patronim):
        super().__init__("Pop", "Popov")
        self.patronim = patronim

child = Child("Popuch")
print(child.name)
print(child.surname)
print(child.patronim)
"""
# 3 задание 
from abc import ABC, abstractclassmethod
class Stationery:
    def __init__(self, title):
        self.title = title 
    
class MyAbstractClass(ABC):
    @abstractclassmethod
    def draw(self):
     print("Запуск отрисовки!")
class Pen(Stationery, MyAbstractClass):
    def draw(self):
        print("Принадлежность иммет синюю отрисвоку")

class Pencil(Stationery, MyAbstractClass):
    def draw(self):
        print("Принадлежность имеет серую отрисовку!")
class Handle(Stationery, MyAbstractClass):
    def draw(self):
        print("Принадлежность имеет жирную отрисовку цвета маркера")

pen = Pen("Ручка")
pen.draw()
pencil = Pencil("карандаш")
pencil.draw()
handle = Handle("маркер")
handle.draw()