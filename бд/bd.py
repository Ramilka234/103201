import sqlite3
# 139 task

# with sqlite3.connect("PhoneBook.db") as db:
#     cursor=db.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
# id integer PRIMARY KEY,
# Firstname text NOT NULL,
# Surname text NOT NULL,
# Phone_number integer);""")
# db.close()
# 140 task
# with sqlite3.connect("PhoneBook.db") as db:
#     cursor=db.cursor()

# def menu():
#     oth = int(input("Main Menu\n\n1) View phone book\n2) Add to phone book\n3) Search for surname\n4) Delete person from phone book\n5) Quit\n\nEnter your selection: "))
#     if oth == 1:
#         cursor.execute("SELECT * FROM Names")
#         for x in cursor.fetchall():
#             print(x)
#         return menu()
        
#     elif oth == 2:
#         newID = int(input("Enter ID number: "))
#         newame = input("Enter Firstname: ")
#         newSurname = input("Enter Surname: ")
#         newNumber = int(input("Enter phone number: "))
#         cursor.execute("""INSERT INTO Names(id, Firstname, Surname, Phone_number)
#         VALUES(?, ?, ?, ?)""",(newID, newame, newSurname, newNumber))
#         db.commit()
#         return menu()
#     elif oth == 3:
#         surn = input("Enter Surname: ")
#         cursor.execute(f"SELECT * FROM Names WHERE Surname = '{surn}'")
#         for x in cursor.fetchall():
#             print(x)
#         return menu()
#     elif oth == 4:
#         searchid = (input("Enter id: "))
#         cursor.execute(f"DELETE FROM Names WHERE id= {searchid}")
#         return menu()
#     elif oth == 5:
#         print("Your closed menu!")
#     else:
#         print("Disable others!")
#         return menu()

# menu()
# db.close()

# 141 task 
# with sqlite3.connect("BookInfo.db") as db:
#     cursor=db.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
# Name text NOT NULL,
# Place_of_Birth text NOT NULL);""")
# cursor.execute("""INSERT INTO Authors(Name, Place_of_Birth)
# VALUES("Agatha Christie","Torquay")""")
# db.commit()
# cursor.execute("""INSERT INTO Authors(Name, Place_of_Birth)
# VALUES("Cecelia Ahern","Dublin")""")
# db.commit()
# cursor.execute("""INSERT INTO Authors(Name, Place_of_Birth)
# VALUES("J. K. Rowling","Bristol")""")
# db.commit()
# cursor.execute("""INSERT INTO Authors(Name, Place_of_Birth)
# VALUES("Oscar Wilde","Dublin")""")
# db.commit()

# cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
# id integer PRIMARY KEY,
# Title text NOT NULL,
# Author text NOT NULL,
# Date_Published integer);""")

# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(2, "Harry Potter and the chamber of secrets", "J. K. Rowling", 1998)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(3, "Harry Potter and the prisoner of Azkaban", "J. K. Rowling", 1999)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(4, "Lyrebird", "Cecelia Ahern", 2017)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(5, "Perfect", "Cecelia Ahern", 2017)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(6, "The marble collector", "Cecelia Ahern", 2016)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(7, "The murder on the links", "Agatha Christie", 1923)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(8, "The picture of Dorian Gray", "Oscar Wilde", 1890)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(9, "The secret adversary", "Agatha Christie", 1921)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(10, "The seven dials mystery", "Agatha Christie", 1929)""")
# db.commit()
# cursor.execute("""INSERT INTO Books(id, Title, Author, Date_Published)
# VALUES(11, "The year I met you", "Cecelia Ahern", 2014)""")
# db.commit()
# db.close()

#141 task
# with sqlite3.connect("BookInfo.db") as db:
#     cursor=db.cursor()

# cursor.execute("SELECT * FROM Authors")
# for x in cursor.fetchall():
#     print(x)

# oth = input("Введите место рождения ")
# cursor.execute(f"SELECT Books.Title, Books.Date_Published, Authors.Name FROM Books, Authors WHERE Authors.Name=Books.Author AND Authors.Place_of_Birth =?",[oth])
# for x in cursor.fetchall():
#     print(x)
# cursor.close()

#142
# with sqlite3.connect("BookInfo.db") as db:
#     cursor=db.cursor()
# oth = int(input("Введите год "))
# cursor.execute(f"SELECT * FROM Books WHERE Date_Published > {oth} ORDER BY Date_Published ")
# for x in cursor.fetchall():
#     print(x)
# cursor.close()

#143

# with sqlite3.connect("BookInfo.db") as db:
#     cursor=db.cursor()
# oth = (input("Введите автора "))
# cursor.execute("SELECT * FROM Books WHERE Author = ?",[oth])
# file = open("book.txt","w")
# for x in cursor.fetchall():
#     for y in x:
#         file.write (f"{str(y)} - ")
#     file.write("\n")
# file.close()
# cursor.close()

#144
# from tkinter import *
# from tkinter import ttk
# def Add():
#     with sqlite3.connect("TestScores.db") as db:
#         cursor=db.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS Student(
#     Name text NOT NULL,
#     Grade text NOT NULL);""")
#     oth_st = st_entry_box.get()
#     oth_name = name_entry_box.get()
#     cursor.execute(f"""INSERT INTO Student(Name, Grade) 
#         VALUES(?, ?)""",(oth_name, oth_st))
#     db.commit()
#     cursor.close()
# def Clear():
#     st_entry_box.delete(0,END)
#     name_entry_box.delete(0,END)
# window = Tk()
# window.title("Window Title")
# window.geometry("450x100")
# name_label = Label(text = "Enter student's name: ")
# name_entry_box = Entry (text = 0)
# st_label = Label(text = "Enter student's grade: ")
# st_entry_box = ttk.Entry()
# add_button = Button(text = "Add", command = Add)
# clear_button = Button(text = "Clear", command = Clear)
# st_label.place(x = 60, y = 20, width = 120, height = 25)
# st_entry_box.grid(column=0, row=1, padx=210, pady=26, sticky=EW)
# clear_button.place(x = 120, y = 50, width = 80, height = 25)
# add_button.place(x = 30, y = 50, width = 80, height = 25)
# name_label.place(x = 60, y  = 5, width = 120, height = 20)
# name_entry_box.place(x = 210, y = 5, width = 120, height = 30 ) 
# window.mainloop()