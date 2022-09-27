"""

Задание 7


Выведите все элементы списка с четными индексами.

Пример:
list1=[0, 1, 2, 3, 4, 5, 6]
>>[1, 3, 5]

"""
list1=[0, 1, 2, 3, 4, 5, 6]
list2=[]
for index,item in enumerate(list1):
    if index%2==0:
        list2.append(item)
        print(list2)
