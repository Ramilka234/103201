"""

Задание 5

Дан список чисел, необходимо удалить все вхождения числа 20 из него.

Пример:
list1 = [5, 20, 15, 20, 25, 50, 20]
>> [5, 15, 25, 50]
"""
list1 = [5, 20, 15, 20, 25, 50, 20]
for index,item in enumerate(list1):
    if item == 20:
     del list1[index]
     print(list1)