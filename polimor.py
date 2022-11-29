# 1 задание 
"""
class Batary:
    def __init__(self):
        self.capacity = []
        self.max_charge = 5

    def charge(self, others = ")"):
        if len(self.capacity) < self.max_charge:
            self.capacity.append(others)
        else:
            print("Батарея заряжена")
    def discharge(self, others = ")"):
        if len(self.capacity)>0:
            self.capacity.pop()
            return self 
        else:
            print("Батарея разряжена")

    
    def __str__(self, others = ")"):
        while len(self.capacity) < self.max_charge:
            self.capacity.append(others)
        return f'{self.capacity} - максимально заряженная батарея.'

bat = Batary()
bat.charge()
print(bat.capacity)
"""
# 2 задание 
"""
class Queue:
    def __init__(self ):
        self.inside = []
        self.strok = ''

    def __str__(self):
        for index , i in enumerate(self.inside) :
            if index != len(self.inside)-1:
                self.strok += f'{self.inside[index]} => {self.inside[index+1]}'
            else:
                self.strok = f'{self.inside[index]}'
        return f'{self.strok}'
        
    def add(self, name ):
        self.inside.append(name)

    def take_out(self):
        del self.inside[0]

    def __add__(self, name):
        self.inside.append(name)

    def __sub__(self, others):
        for index, i in enumerate(self.inside):
            if i == others:
                del self.inside[index]
        return self 

    def __isub__(self, others):
        for index, i in enumerate(self.inside):
            if i == others:
                del self.inside[index]
        return self 

    def __iadd__(self, name):
        self.inside.append(name)
    
que = Queue()
que.add("ramil")
que.add('pop')
que + 'lip'
que.take_out()
que - 'pop' 
print(que)
"""
# 3 задание 
"""
import numpy as np 
class Matrix:
    def __init__(self, znach = list):
        self.znach = znach 
    def __str__(self):
        str1 = ''
        for  i in self.znach:
            a = ' '.join(map(str,i))
            str1 += f' {a}\n'
        return f'{str1} '

    def __add__(self, other):
        A = np.array(self.znach)
        B = np.array(other.znach)
        C = A + B
        str1 = ''
        for  i in C:
            a = ' '.join(map(str,i))
            str1 += f' {a}\n'
        return f'{str1} '
matr1 = Matrix([[3,4,6], [4,6,2]])
matr2 = Matrix([[3,4,6], [4,6,2]])
res = matr1 + matr2
print(matr1)
print(res)
"""