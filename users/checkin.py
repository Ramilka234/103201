def login(username,password, user):
    for i in range(0, len(user)):
        if user[i]["Username"] == username and user[i]["Password"] == password:
            print("Доступ разрешен!")
            break 
        elif user[i]["Username"] != username and user[i]["Password"] == password:
            print("Доступ запрещен, неправильный логин!")
            break 
        elif user[i]["Username"] == username and user[i]["Password"] != password:
            print("Доступ запрещен, неправильный пароль!")
            break 
        elif user[i]["Username"] != username and user[i]["Password"] != password:
            user.append({"Username": username, "Password": password})
            print("Регистрация прошла успешно!")
            break 

def del_user(d, key):
    r = dict(d)
    del r[key]
    return r

