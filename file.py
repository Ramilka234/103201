#105 задания 
"""
file = open("Numbers.txt", "w")
file.write("5,")
file.write("6,")
file.write("7,")
file.write("8,")
file.write("9")
file.close()
file = open("Numbers.txt", "r")
print(file.read())
"""
#106 задание 
"""
file = open("Names.txt","w")
file.write("Anton\n")
file.write("Petr\n")
file.write("Alik\n")
file.write("Nikita\n")
file.write("Pop\n")
file.close()
"""
#107 задание 
"""
file = open("Names.txt","r")
print(file.read())
file.close()
"""
# 108 задание 
"""
file = open("Names.txt","a")
file.write(input("Введите имя "))
file.close()
"""
# 109 задание 
"""
print("1) Create a new file\n2) Display the file\n3) Add a new item to the file")
otv = int(input("Make a selection 1, 2 or 3: "))
if otv == 1:
    file = open("Subject.txt","w")
    file.write(input("Введите название предмет"))
    file.write("\n")
    file.close()
elif otv == 2:
    file =open("Subject.txt","r")
    print(file.read())
    file.close()
elif otv == 3:
    file = open("Subject.txt","a")
    file.write(input("Введите название нового предмета "))
    file.write("\n")
    file.close()
    file = open("Subject.txt","r")
    print(file.read())
    file.close()
else:
    print("Вы ввели некоректное значение ")
"""
"""
file = open("Names.txt","r")
print(file.read())
file.close()
file = open("Names.txt","r")
a = input("Введите имя, которое нужно вычеркнуть")
file1 = open("Names2.txt","w")
for i in file:
    if i == a:
        continue
    file1.write(i)
file.close()
file.close()
"""
# 111 задание 
import csv

file = open ("Books.csv", "w")
book0 = "To Kill a Mockingbird, Harper Lee, 1960\n"
book1 = "A Brief History of Time, Stephen Hawking, 1988\n"
book2 = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
book3 = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
book4 = "Pride and Prejudice, Jan Austen, 1813\n"
file.write(str(book0))
file.write(str(book1))
file.write(str(book2))
file.write(str(book3))
file.write(str(book4))
file.close()
#112 задание
"""
file = open("Books.csv","a")
book = input("Enter book: ")
autor = input("Enter autor: ")
year = input("Enter year: ")
newbook = book + ", " + autor + ", " + year + "\n"
file.write(str(newbook))
file.close()
file = open("Books.csv","r")
for row in file:
    print(row)
"""
# 113 задание 
"""
kol = int(input("Какое количество книг вы хотите добавить "))
file = open("Books.csv","a")
i = 1
while i <= kol:
    i += 1
    book = input("Enter book: ")
    autor = input("Enter autor: ")
    year = input("Enter year: ")
    newRecord = book + ", " + autor + ", " + year + "\n"
    file.write(str(newRecord))
file.close()

file = open("Books.csv","r")
search = input("Enter the autor you are searching for: ")
reader = csv.reader(file)
for row in file:
    if search in str(row):
        print(row)
"""
#114 задание 
"""
file = open("Books.csv","r")
n = int(input("Введите начальный год "))
k = int(input("Введите конечный год "))
prom = []
for j in range(n,k):
    prom.append(j)
reader = csv.reader(file)
for row in file:
    for o in prom:
        if str(o) in str(row) :
            print(row)
"""
# 115 задание 
"""
file = open("Books.csv","r")
for index, row in enumerate(file):
    print(f"{index} - {row}")
"""
# 116 задание 
"""
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
for index, i in enumerate(tmp):
    print(f"{index} - {i}")
a = int(input("Введите номер списка, который хотите исключить "))
del tmp[a]
b = int(input("Введите номер списка, который хотите изменить "))
tmp[a] = input()
file.close()
file = open("Books.csv","w")
for i in tmp:
    file.write(str(i))
file.close()
"""
#117 задание 
"""
import random
name = input("Введите ваше имя: ")
question_prompts = [

["What color are apples?\n(a)Red/Green\n(b)Orange \n(c)Violet/Green\n(d)Black/Orange", "a"],

["What color are bananas?\n(a)Red/Green\n(b)Yellow \n(b)Orange \n(a)Violet/Green", 'b'],

["What Month is Christmas?\n(a)September \n(b)December \n(c)October \n(d)November", 'b'],

["What color are Rice?\n(a)Red/Green\n(b)Yellow\n(c)Red/Green\n(d)Yellow", 'b'],

["What animal can run faster than Lion?\n(a)Man\n(b)Dear\n(c)Red/Green\n(d)Yellow", 'b'],
     
["How many continents in the World ?\n(a) Seven\n(b) Nine\n(c)Red/Green\n(d)Yellow", 'a'],

["How many colors rainbow has?\n(a)Seven\n(b)Five\n(c)Red/Green\n(d)Yellow", 'a'],

["What is my name?\n(a) Nick\n(b)Chioma\n(c)Tiger\n(d)Greatness", 'a'],

["What year did Pandemic occur?\n(a)2020\n(b)2019\n(c)2021\n(d)2023", 'a'],

["How old is the earth approximately?\n(a)6b years\n(b)6.4b years\n(c)6b years\n(d)6.4b years", 'b']


]

count = 0


sample = random.sample(question_prompts, 2)
quest = ' '
ans = ' '
for i, j in sample:
    quest += i 
    print(i)
    answer = input("Enter your answer: ").lower()
    ans += answer
    if answer == j:
        count += 1
        print("Right, Your score: ", count)
        print('')
    else:
        print("Wrong, correct answer is: ", j)
        print()

print("You got", count, "out of", len(sample), "questions")
file = open("game.csv","a")
newPlayer = name + "," + quest + ',' + ans + ',' + str(count) + "\n"
file.write(str(newPlayer))
file.close()
"""