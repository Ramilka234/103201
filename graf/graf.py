from tkinter import *
#124 task 
"""
def Call():
    num = entry_box.get()
    msg = Label(window, text = f"Hello  {num} ")
    msg.place(x = 30, y = 50)
    button["bg"] = "blue"
    button["fg"] = "white"
    entry_box ["bg"] = "red"
    entry_box ["fg"] = "white"
window = Tk()
window.title("Window Title")
window.geometry("450x100")
label = Label(text = "Enter name: ")
entry_box = Entry (text = 0)
button = Button(text = "Press me", command = Call)
button.place(x = 30, y = 20, width = 120, height = 25)
label.place(x = 10, y  = 5, width = 100, height = 20   )
entry_box.place(x = 100, y = 5, width = 100, height = 20 ) 
window.mainloop()
"""
#125 задание 
"""
import random 
def Call():
    msg = Label(window, text = random.randrange(7))
    msg.place(x = 30, y = 50)
    button["bg"] = "blue"
    button["fg"] = "white"

window = Tk()
window.title("Window Title")
window.geometry("450x100")
button = Button(text = "Press me", command = Call)
button.place(x = 30, y = 20, width = 120, height = 25)
window.mainloop()
"""
# 126 task 
"""

def Suma():
    a = entry_box.get()
    b = output_box["text"]
    a = int(a)
    b = int(b)
    RBB = a + b
    output_box["text"] = RBB

def Chistka():
    RBB = 0;
    output_box["text"] = 0
    entry_box.delete(0, END)

window = Tk()
window.title('СУММА')
window.geometry("600x200")

label = Label(text = "Жду число")
label.place(x=10,y=10,width = 220,height = 20)

entry_box = Entry(text=0)
entry_box.place(x=50,y=40,width = 220,height = 30)

output_box = Message(text=0)
output_box ["bg"] = "green"
output_box.place(x=275,y=40,width = 220,height = 30)

button1 = Button(text = "Сложить",command = Suma)
button1.place(x = 176,y = 90,width = 100,height = 30)

button2 = Button(text = "Очистить",command = Chistka)
button2.place(x = 50,y = 90,width = 100,height = 30)
window.mainloop()
"""
#127 task 
"""
from tkinter import ttk
 
 

def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])
 
 

def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)
 
window = Tk()
window.title("Window Title")
window.geometry("300x250")
window.columnconfigure(index=0, weight=4)
window.columnconfigure(index=1, weight=1)
window.rowconfigure(index=0, weight=1)
window.rowconfigure(index=1, weight=3)
window.rowconfigure(index=2, weight=1)
 
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
 
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")
 
ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
 
window.mainloop()
"""
# 128 task 

def km():
    num = entry_box.get()
    msg = Label(window, text = f"{float(num) * 0.6214} ml" )
    msg.place(x = 30, y = 50)
def ml():
    num1 = entry_box1.get()
    msg = Label(window, text = f"{float(num1) * 1.6093} km" )
    msg.place(x = 20, y = 140)

window = Tk()
window.title("Window title")
window.geometry("300x250")
label = Label(text = "Enter a km: ")
entry_box = Entry (text = 0)
button = Button(text = "Press me", command = km)
button.place(x = 30, y = 20, width = 120, height = 25)
label.place(x = 10, y  = 5, width = 100, height = 20   )
entry_box.place(x = 100, y = 5, width = 100, height = 20 )


label1 = Label(text = "Enter a ml: ")
entry_box1 = ttk.Entry()
entry_box1.grid(column=2, row=1, padx=100, pady=80, sticky=EW)
button1 = Button(text = "Press me", command = ml)
button1.place(x = 20, y = 100, width = 120, height = 25)
label1.place(x = 20, y  = 75, width = 100, height = 20   )
window.mainloop()

#129 task
"""
from tkinter import ttk
import numbers
 

def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])
 
 

def add():
    new_language = language_entry.get()
    if float(new_language) % 1 == 0 :
        languages_listbox.insert(0, new_language)
    else:
        language_entry.delete(0,END)
 
window = Tk()
window.title("Window Title")
window.geometry("300x250")
window.columnconfigure(index=0, weight=4)
window.columnconfigure(index=1, weight=1)
window.rowconfigure(index=0, weight=1)
window.rowconfigure(index=1, weight=3)
window.rowconfigure(index=2, weight=1)
 
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
 
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")
 
ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
 
window.mainloop()
"""
# 130 
"""
import csv 
from tkinter import ttk
import numbers
 

def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])
 
 

def add():
    new_language = language_entry.get()
    if float(new_language) % 1 == 0 :
        languages_listbox.insert(0, new_language)
    else:
        language_entry.delete(0,END)

def cs():
    tmp_list = languages_listbox.get(0,END)
    file = open("list.csv","a")
    for i in tmp_list:
        file.write(str(i))
        file.write("\n")
    file.close()

window = Tk()
window.title("Window Title")
window.geometry("300x250")
window.columnconfigure(index=0, weight=4)
window.columnconfigure(index=1, weight=1)
window.rowconfigure(index=0, weight=1)
window.rowconfigure(index=1, weight=3)
window.rowconfigure(index=2, weight=1)
 
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
 
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")
 
ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
ttk.Button(text="создать файл csv", command=cs).grid(row=2, column=2, padx=5, pady=5)
window.mainloop()
"""
# 131 task 
"""
import csv 
from tkinter import ttk
def css():
    new_name = name_entry.get()
    new_age = age_entry.get()
    file = open("nmag.csv","w")
    file.write(str(new_name))
    file.write("\n")
    file.write(str(new_age))
    file.write("\n")
    file.close()
window = Tk()
window.title("Window title")
window.geometry("300x250")
label_name = Label(text = "Enter name: ")
name_entry = ttk.Entry()
name_entry.grid(column=2, row=0, padx=6, pady=6, sticky=EW)
label_age = Label(text = "Enter age: ")
age_entry = ttk.Entry()
age_entry.grid(column=2, row=1, padx=7, pady=7, sticky=EW)
ttk.Button(text="Создать файл ", command=css).grid(row=2, column=1, padx=5, pady=5)
label_name.place(x = 10, y  = 5, width = 100, height = 20   )
label_age.place(x = 10, y  = 50, width = 100, height = 20   )



window.mainloop()
"""
#132 task 
"""
import csv 
from tkinter import ttk
def css():
    new_name = name_entry.get()
    new_age = age_entry.get()
    file = open("nmag.csv","a")
    
    a = new_name + "," + new_age
    file.write(str(a))
    file.close()
def read():
    file = open("nmag.csv","r")
    for index, row in enumerate(file):
        languages_listbox.insert(1, row)
window = Tk()
window.title("Window title")
window.geometry("500x350")
label_name = Label(text = "Enter name: ")
name_entry = ttk.Entry()
name_entry.grid(column=2, row=0, padx=6, pady=6, sticky=EW)
label_age = Label(text = "Enter age: ")
age_entry = ttk.Entry()
age_entry.grid(column=2, row=1, padx=7, pady=7, sticky=EW)
ttk.Button(text="Добавтиь в файл ", command=css).grid(row=2, column=1, padx=5, pady=5)
label_name.place(x = 10, y  = 5, width = 100, height = 20   )
label_age.place(x = 10, y  = 50, width = 100, height = 20   )
ttk.Button(text="Вывести содержимое файла ", command=read).grid(row=2, column=2, padx=5, pady=5)
languages_listbox = Listbox()
languages_listbox.grid(row=3, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

window.mainloop()
"""
# 133 task 
"""
from tkinter import ttk
window = Tk()
def Call():
    num = name_entry.get()
    msg = Label(window, text = f"Hello  {num} ")
    msg.place(x = 140, y = 200)

window.configure(background = "black")
window.title("Window title")
window.geometry("500x350")

logo = PhotoImage(file = "Logo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 100, y = 20, width = 200, height = 120)


label = Label(text = "Enter name: ")
entry_box = Entry (text = 0)
button = Button(text = "Press me", command = Call)
button.place(x = 20, y = 200, width = 120, height = 25)
label.place(x = 35, y  = 150, width = 100, height = 20   )
entry_box.place(x = 140, y = 200, width = 120, height = 25 ) 
name_entry = Entry(text = 0 )
name_entry.place(x = 140, y  = 150, width = 120, height = 25 )
label ["bg"] = "black"
label ["fg"] = "white"
entry_box["bg"] = "white"
entry_box ["fg"] = "white"
button["bg"] = "gray"
button["fg"] = "black"
window.mainloop()
"""
# 134 
"""
import random
def plus():
    num = one_label['text']
    num2 = two_label['text']
    otv = otvet_entry.get()
    if int(num) + int(num2) == int(otv):
        photo = PhotoImage(file = "gal.gif")
        photobox = Label(window, image = photo)
        photobox.image = photo
        photobox.place(x = 50, y = 50, width = 200, height = 120)
    else:
        photo = PhotoImage(file = "kres.gif")
        photobox = Label(window, image = photo)
        photobox.image = photo
        photobox.place(x = 50, y = 50, width = 200, height = 120)
def next():
    one_label["text"] = random.randrange(10,50)
    two_label["text"] = random.randrange(10,50)
window = Tk()
window.title("window tittle ")
window.geometry("500x350")
one_label = Label (text = random.randrange(10,50))
two_label = Label (text = random.randrange(10,50))
one_label.place(x = 10, y = 15, width = 120, height = 25 )
two_label.place(x = 80, y = 15, width = 120, height = 25 )
button = Button(text = "Press me ", command = plus)
button.place(x = 20, y = 200, width = 120, height = 25)
otvet_entry = Entry(text = 0 )
otvet_entry.place(x = 20, y  = 150, width = 120, height = 25 )
button = Button(text = "Next ", command = next)
button.place(x = 120, y = 200, width = 120, height = 25)

window.mainloop()
"""
#135
"""
import csv 
from tkinter import ttk
import numbers
 

def color():
    selection = languages_listbox.curselection()
    for i in selection:
        if i == 0:
            window.configure(background = "purple")
        elif i == 1:
            window.configure(background = "red")
        elif i == 2:
            window.configure(background = "black")
        elif i == 3:
            window.configure(background = "yellow")
 



window = Tk()
window.title("Window Title")
window.geometry("300x250")
window.columnconfigure(index=0, weight=4)
window.columnconfigure(index=1, weight=1)
window.rowconfigure(index=0, weight=1)
window.rowconfigure(index=1, weight=3)
window.rowconfigure(index=2, weight=1)
 

languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
 
languages_listbox.insert(END, "purple")
languages_listbox.insert(END, "red")
languages_listbox.insert(END, "black")
languages_listbox.insert(END, "yellow")
 
ttk.Button(text="Click me ", command=color).grid(row=2, column=1, padx=5, pady=5)

window.mainloop()
"""
#136 
"""
from tkinter import ttk
def ls():
    
    num = name_entry.get()
    num1 = selectName.get()
    
    if "Gay" == num1:
        lst.append(num , )
        lst.append("Gay")
    elif "Girl" == num1:
        lst.append(num , )
        lst.append("Girl")
    print(lst)
    
lst = [ ]
window = Tk()
window.title("Window Title")
window.geometry("500x350")
label_name = Label(text = "Enter name: ")
name_entry = Entry(text = 0 )
name_entry.place(x = 50, y = 20, width = 100, height = 25)
label_name.place(x=0, y = 20, width = 80, height = 100 )
selectName = StringVar(window)
selectName.set("Pol")
namesList = OptionMenu(window, selectName, "Gay", "Girl")
namesList.place(x = 130, y = 20)
button = Button(text = "Press me  ", command = ls)
button.place(x = 120, y = 200, width = 120, height = 25)
window.mainloop()
"""
#137 
"""
from tkinter import ttk
def ls():
    
    num = name_entry.get()
    num1 = selectName.get()
    
    if "Gay" == num1:
        lst.append(num , )
        lst.append("Gay")
        file = open("lst.txt", "a")
        file.write(num)
        file.write("\n")
        file.write("Gay")
    elif "Girl" == num1:
        lst.append(num , )
        lst.append("Girl")
        file = open("lst.txt", "a")
        file.write(num)
        file.write("\n")
        file.write("Girl")
    print(lst)
def read():
    file = open("lst.txt","r")
    for index, row in enumerate(file):
        languages_listbox.insert(1, row)
lst = [ ]
window = Tk()
window.title("Window Title")
window.geometry("500x350")
label_name = Label(text = "Enter name: ")
name_entry = Entry(text = 0 )
name_entry.place(x = 50, y = 20, width = 100, height = 25)
label_name.place(x=0, y = 20, width = 80, height = 100 )
selectName = StringVar(window)
selectName.set("Pol")
namesList = OptionMenu(window, selectName, "Gay", "Girl")
namesList.place(x = 130, y = 20)
button = Button(text = "Press me  ", command = ls)
button.place(x = 120, y = 100, width = 120, height = 25)
languages_listbox = Listbox()
languages_listbox.place(x = 50, y = 200, width=120, height = 150 )
list_button = Button(text = "open file  ", command = read)
list_button.place(x = 190, y = 200, width = 120, height = 25)
window.mainloop()
"""
#138 
"""
import random
def ph():
    otv = otvet_entry.get()
    if otv == "1":
        photo = PhotoImage(file = "1.gif")
        photobox = Label(window, image = photo)
        photobox.image = photo
        photobox.place(x = 50, y = 50, width = 600, height = 360)
    elif otv == "2":
        pho = PhotoImage(file = "2.gif")
        photobox = Label(window, image = pho)
        photobox.image = pho
        photobox.place(x = 50, y = 50, width = 600, height = 360)
    elif otv == "3":
        ph = PhotoImage(file = "3.gif")
        photobox = Label(window, image = ph)
        photobox.image = ph
        photobox.place(x = 50, y = 50, width = 600, height = 360)

window = Tk()
window.title("window tittle ")
window.geometry("1000x800")
photo = PhotoImage(file = "1.gif")
photobox = Label(window, image = photo)
photobox.image = photo
photobox.place(x = 50, y = 50, width = 600, height = 360)
button = Button(text = "Press me ", command = ph)
button.place(x = 20, y = 200, width = 120, height = 25)
otvet_entry = Entry(text = 0 )
otvet_entry.place(x = 20, y  = 150, width = 120, height = 25 )


window.mainloop()
"""
