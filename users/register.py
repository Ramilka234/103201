import string

def checker(list, dan):
    for index, article  in enumerate(list):
        index += 1 
        if dan == article:
            a = "Вы уже зарегистрированы! "
        else:
            a = "Вы еще не зарегестрированы!"
    return a 
            

def validate(dan):
    if dan.isalpha():
        a = "Вы ввели корректные данные!"
    else:
        a = "Вы ввели недопустимые символы!"
    return a 
def register(lis, dann = input() ):
    if checker(lis,dann) == "Вы еще не зарегестрированы!"  and  validate(dann) == "Вы ввели корректные данные!" :
        lis.append(dann)
    else:
        print("Error")



