'''

Задание 8

Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.


Пример:
list=[0, 7, 43, 10, -4, 2, 28, 7, 43, 7, 0]
>> 43 2

'''
list=[0, 7, 43, 10, -4, 2, 28, 7, 43, 7, 0]
a = max(list)
b = list.index(a)
print(a,b)


    
