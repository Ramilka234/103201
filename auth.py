import users.checkin


dct = [{"Username" : "Ramil", "Password" : "123456", "Username" :"Lia", "Password" : "qwerty" }]

def init():
    users.checkin.login(input("Введите логин: "), input("Введите пароль: "), dct)

init()
