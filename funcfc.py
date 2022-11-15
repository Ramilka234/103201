# 1 задание
"""
def calculate(a, b , c =""):
    if c == "+":
        print(eval(f"{a} {c} {b}"))
    elif c == "-":
        exec(print(f"{a} {c} {b}"))
    elif c == "*":
        print(eval(f"{a} {c} {b}"))
    elif c == "/":
        print(eval(f"{a} {c} {b}"))
    else:
        return print("Вы ввели неправильную операцию!")
calculate(3, 6 ,"*")
"""
# 2 задание
"""
import re 
s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']

def preob(x):
    for index, article in enumerate(x):    
        x[index] = re.sub(r'[0-9|!|+]',r'',article.title())
    return x

print(preob(s))
"""

# 3 задание 
"""
data = [i for i in range(1, 21)]
def honest(list):
    for index, number in enumerate(list):
        if number%2 != 0:
            del list[index]
    return list
print(honest(data))
"""

# 4 задание 
"""

def cesar(txt, s): 
    result = ""  
    for i in range(len(txt)): 
        char = txt[i] 
        if(char.isupper()): 
            result += chr((ord(char) + s - 64) % 26 + 65) 
        else: 
            result += chr((ord(char) + s - 96) % 26 + 97) 
    return result 

a = "abcd"
b =3
print(cesar(a,b))
"""

# 5 задание 
"""
from random import sample
a = sample(range(0, 10), 10)
def coutdown(list):
    list.sort()
    list.reverse()
    for i in list:
        print(i, end = " ")
    print("Пуск!")
print(coutdown(a))
"""
#6 задание
"""
import string

def alphabet():
    index = 0 
    ind = 0 
    for alph in  string.ascii_lowercase:
        index += 1
        print(index, alph)
    dct = {i: a for i,a in zip(range(1,27), string.ascii_lowercase)}
    print(dct)

alphabet()
"""
# 7 задание 
"""
def decorator(x):
    def wrapper():      
        print(f"Hello {x()}!")
    return wrapper

def get_name( ):
    name = input('Введите имя')
    return name

@decorator
def get_name():
    name = input('Введите имя ')
    return name

get_name()
"""

# 8 задание 

"""
def decorator(x):
    def wrapper(*args):
        print(f"<p>{x(*args)}</p>")
    return wrapper

@decorator
def render_input(field):
  return f'<input id="id_{field}" name="{field}">'

username = render_input('username')
print(username)
"""