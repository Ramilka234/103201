"""1 задание
class cat:
    def __init__(self,name,age,color,milota=0):
        self.age = age
        self.name = name 
        self.color = color
        self.milota = milota
    def myau(self):
        self.milota += 10
    def murlyk(self):
        self.milota += 20
    def ryg(self):
        self.milota = 0 
kuzya = cat("kuzya",3,"gray")
kuzya.myau()
print(kuzya.milota)
kuzya.murlyk()
print(kuzya.milota)
 """
 # 2 задание

"""
class Good:
    def __init__(self,name,price,weight,cost=0):
        self.name = name 
        self.price = price
        self.cost = cost
        self.weight = weight
    def calc(self):
        self.cost = self.price *self.weight

apple = Good('apple', price = 100, weight = 1.5)
pear = Good('pear', price = 120, weight = 0.8)

apple.calc()
print(apple.cost)
"""

#3 задание 
"""
class Car:
    def __init__(self,color,marka,kuzov,korobka,speed=0):
        self.color = color 
        self.marka = marka 
        self.kuzov = kuzov
        self.korobka = korobka
        self.speed = speed 
    def start(self):
        self.speed = 5 
        print(f"speed = {self.speed} km/h")
    def stop(self):
        self.speed = 0 
        print(f"speed = {self.speed} km/h")
    def turn(self, i = ""):
        if i == "left":
            print("Машина повернула налево")
        elif i == "right":
            print("Машина повернула направо")
        elif i == "back":
            print("Машина повернула назад")
        elif i == "top":
            print("Машина едет прямо ")
    def speed_up(self, i=1):
        print(f'speed = {self.speed + i} km/h')
        self.speed += i
    def speed_down(self, i=1):
        if self.speed == 0:
            print('speed = 0 km/h')
        else:
            print(f'speed = {self.speed - i} km/h')
            self.speed -= i
    def beep(self):
        print("BEEEEP")
    
truck = Car("blue","Bmw", "Hetch","auto")
truck.start()
truck.stop()
truck.turn("right")
truck.start()
truck.speed_up()
truck.speed_up()
truck.speed_up()
truck.speed_down()
truck.speed_down()
truck.speed_down()
truck.beep()
truck.stop()

car = Car("Black", "Lada", "Sedan", "mehanika")
car.start()
car.stop()
truck.turn("right")
car.start()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_down()
car.speed_down()
car.speed_down()
car.beep()
car.stop()
"""
# 4 задание 
"""
class Car:
    def __init__(self,color,marka, gruz, kuzov,korobka,speed=0):
        self.color = color 
        self.marka = marka 
        self.kuzov = kuzov
        self.korobka = korobka
        self.speed = speed 
        self.gruz = gruz
    def start(self):
        self.speed = 5 
        print(f"speed = {self.speed} km/h")
    def stop(self):
        self.speed = 0 
        print(f"speed = {self.speed} km/h")
    def turn(self, i = ""):
        if i == "left":
            print("Машина повернула налево")
        elif i == "right":
            print("Машина повернула направо")
        elif i == "back":
            print("Машина повернула назад")
        elif i == "top":
            print("Машина едет прямо ")
    def speed_up(self, i=1):
        if self.gruz == "passenger": 
            self.speed += i 
            while self.speed <= 80:
                print(f'speed = {self.speed } km/h')
                break
            if self.speed > 80:
                print("Вы превысили ограничение в скорости!") 
        elif self.gruz == "truck": 
            self.speed += i
            while self.speed <= 60:   
                print(f'speed = {self.speed } km/h')
                break
            if self.speed > 60:
                print("Вы превысили ограничение в скорости!")
        
    def speed_down(self, i=1):
        if self.speed == 0:
            print('speed = 0 km/h')
        else:
            print(f'speed = {self.speed - i} km/h')
            self.speed -= i
    def beep(self):
        print("BEEEEP")

car = Car("Black", "Lada", "passenger", "Sedan", "mehanika") 
car.start()
car.start()
car.speed_up(9)

truck = Car("blue","Bmw", "truck", "Hetch","auto")
truck.start()
truck.start()
truck.speed_up(70)
"""

# 5 задание 
"""
from time import sleep
def trafficlight(red = 1, yellow = 0.5, green = 2):
    print("Светофор работает!")
    sleep(red)
    print("Красный!")
    sleep(yellow)
    print("Желтый!")
    sleep(green)
    print("Зеленый!")

trafficlight()
"""