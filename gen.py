#1 задание
#coutdown = (x for x in range(11))
#а)
# for i in reversed(list(coutdown)):
 #   print(i)

#б)
# lst_cout = reversed(list(coutdown))
#while lst_cout != 0 :
 #   print(next(lst_cout))

 # 2 задание 

#import string 

#alf = (i for i in string.ascii_lowercase)
#while alf != "z":
 #   print(next(alf))

# 3 задание
"""
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(10))
print(data)

# задание 4 
 
i = iter(data)
#for x in i:
 #   print(x)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
"""

""" задание 5 


n = [c for c in range(21) if c%2==0]

for i in n :
    print(i)
    """
# задание 5 
"""
import string 

dct = {key : value for key,value in zip(range(1,24), string.ascii_lowercase)}
print(dct)
"""