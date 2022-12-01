# 1 задание 
"""
class Person:
    def __init__(self, name , age, surname ):
        self.__name = name 
        self.__age = age 
        self.__surname = surname
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def surname(self):
        return self.__surname 


    @age.setter 
    def age(self, new_age):
        self.__age = new_age
        return self.__name
human = Person("Pop", 65, "Popov")
print(human.name)
print(human.age)
human.age = 67
print(human.age)
"""
# 2 задание 

from abc import ABC, abstractmethod
class Clotch(ABC):
    def __init__(self,VH):
        self.VH = VH  

    @abstractmethod
    def method(self):
        pass
    

class Coat(Clotch):
    reserved = 0
    def __init__(self): 
        super().__init__(int(input("Введите размер: ")))
        
    def method(self ):
        Coat.reserved += (self.VH/6.5)-0.5
        return Coat.reserved

class Suit(Clotch):
    reserved = 0
    def __init__(self): 
        super().__init__(int(input("Введите рост: ")))
        
    def method(self ):
        Suit.reserved += (self.VH*2)+0.3
        return Suit.reserved

coat = Coat()
print(coat.method())

suit = Suit()
print(suit.method())
suit2 = Suit()
print(suit.method())

# 4 задание 
"""
import task_3

box1 = task_3.Box("details", "Saratov", "Kazan")
box2 = task_3.Box("Metall", "Saratov", "Kazan")
box3 = task_3.Box("Shin", "Saratov", "Kazan")

print(box1.name)
print(box2.name) 
print(box3.name)
print(box1.postcode)

class Truck:
    def __init__(self, marka, korobka, color, capacity = {} ):
        self.marka = marka
        self.korobka = korobka
        self.color = color 
        self.boxes = [ ]
        self.capacity = {("Box") : [ ] }
    
    def __str__(self):
        return f'{self.marka}, {self.capacity}'

    def __add__(self, other):
        self.boxes.append(other)
        self.capacity[("Box")] = self.boxes

    def __sub__(self, other):
        for index, i  in enumerate(self.capacity):
            if i == other:
                del self.capacity[index]

truck1 = Truck("bmw", "auto", "blue")

print(truck1)
truck1 + 'box1'
truck1 + 'box2'
print(truck1)        
"""

