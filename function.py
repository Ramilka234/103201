# 1 задание 
"""
def calc(a,b,c):
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        if b != 0:
            print(a/b)
        else:
            print("На ноль делить нельзя!")
calc(3,0,"/")
"""
# 2 задание
"""
def reverse(a):
    for i in a[::-1]:
        print(i,end = "")
reverse("Hello privet")
"""
# 3 задание
"""
username = ["Andrey", "Nikita", "Sergey"]

def robot_hello(name):
    for i in username:
        if i == name:
            print(f"Hello {name}")
            break
    else:
        username.append(name)
        print(f"Hello {name}, nice to meet you!")

robot_hello("Ranis")
robot_hello("Nikita")
robot_hello("Ranis")
"""
# 4 задание
"""
def count():
    a = 0 
    b = 0
    c = 0
    while a != 10:
        a+= 1 
        if a % 2 == 0:
            b += 1
        else:
            c += 1
    
    print(f"Количество четных {b} \n Количество нечетных {c}")
    
count()
"""
"""
def count(a = 0,b = 0,c = 0 ):
    a +=1
    if a == 11:
        return print(f"Количество четных {b} \n Количество нечетных {c}")
    else:
        if a % 2 == 0:
            b += 1 
        else:
            c += 1
    return count(a,b,c)
    
count()
"""
#5 задание
"""
def Fibonacci(a = 0 , b = 1,sum = 0 ): 
    while b < 100:
        sum =a+b
        print(b, end = " ")
        a,b = b,sum
        
Fibonacci()
"""
"""
def Fibonacci(a = 0, b = 1, sum = 0 ):
    sum = a+b 
    print(b, end = " ")
    a,b = b,sum
    if b > 100:
        return
    return Fibonacci(a,b,sum)
Fibonacci()
"""

# 6 задание
"""
def factorial(n):
    i = 1
    i_1 = 2
    while i_1 <= n:
        i *=  i_1
        i_1 += 1

    print(i)
factorial(5)
"""
"""
def factorial(n, i = 1, i_1 = 1):
    i_1 += 1
    if i_1 > n:
        return print(i)
    i *=  i_1
    return factorial(n, i, i_1)
factorial(5)
"""
# 7 задание
"""
user = [{"Username": "Ramil", "Password": "12345", }]

def login(username, password):
     for i in range(0, len(user)):
        if user[i]["Username"] == username and user[i]["Password"] == password:
            print("Доступ разрешен!")
            break 
        elif user[i]["Username"] != username and user[i]["Password"] == password:
            print("Доступ запрещен, неправильный логин!")
            break 
        elif user[i]["Username"] == username and user[i]["Password"] != password:
            print("Доступ запрещен, неправильный пароль!")
            break 
        elif user[i]["Username"] != username and user[i]["Password"] != password:
            user.append({"Username": username, "Password": password})
            print("Регистрация прошла успешно!")
            break 

login(input("Введите логин: "), input("Введите пароль: "))
"""
# 8 задание 
"""
from random import randint

def prog(a = randint(0, 100), i = 0  ):
    b = int(input())
    i += 1
    if i == 10:
        return print(f"Вы не отгодали число  {a}")
    if a == b:
        return print(f"Вы отгодали число!")
    else:
        if b < a:
            print("Ваше число меньше")
        elif b>a:
            print("Ваше число больше")
    return prog(a,i)
prog()
"""