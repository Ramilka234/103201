class MyException(Exception):
    pass
# 1 задание 

"""
def validator(a = (input("Введите число: ")), c = 0 ):
       try:
        if a.isalpha():
            raise MyException
        a = int(a)
        c = a**2
       except MyException: 
        c = 'Введено не число'
       finally:
        return print(c)


validator()

"""
# 2 задание 
"""
import re 
def check(a = input("Введите слово: "), c = ""):
    try:
        c = re.findall(r'\W',a)
        if c > []:
            raise MyException
    except MyException: 
        a = 'Введены символы'
    finally:
        return print(a)

check()
"""

# 3 задание
""" 
import re 
str="Всем привет! Меня зовут Алексей. Мой email: alexVB@gmail.com. Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru"

def find_email(x):
    result = re.findall(r':\s\w+.\w+.\w+', x)
    return print(result)
find_email(str)
"""

# 4 задание 
"""
import re 
from collections import Counter

def find_log(filename = input("Введите имя файла ")):
    with open(filename, 'r') as file:
        fi = file.readlines()
        res = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]', str(fi) )
        kol = Counter(res)
        return print(kol)
черновик 
        for index, article in enumerate(res):
            cout_1 = int(res[index]).cout()
            cout_2 = int(res[index + 1]).cout()
            if cout_1 > cout_2 :
                temp = article
            else:
                temp = res[index + 1]
    return print(temp)
черновик 
find_log()
"""

# 5 задание 
"""
import re 

def log_dict(filename = input("Введите имя файла ")):
    dct = {}
    with open(filename, 'r') as file:
        fi = file.readlines()
        ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]', str(fi) )
        request = re.findall(r'"\w{3,4}\s',str(fi))
        data = re.findall(r'\d{2}\/\w{3}\/\d+',str(fi))
        url = re.findall(r'\/\w{2}\S\w+\.\w+',str(fi))
        for index,article in enumerate(ip):
            dct = {ip[index]:[request[index],data[index],url[index]]}
            print(dct)
    

log_dict()

                 
"""


