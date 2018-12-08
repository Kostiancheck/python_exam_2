import re
"""
Перевіряємо немер автомобіля (дві великі літери та чотири цифри)
"""
def get_car():
    user_input = input('Номер автомобіля у форматі "АА1234": ')

    while not (re.match(r"^[A-Z]{2}\d{4}$", user_input) ):
        user_input = input('Номер автомобіля у форматі "АА1234": ')
    return user_input

"""
    Написати валідатор ....
    Перевіряємо електронну адресу (Name@gmail.com) на велику літеру спочатку, потім літери та @gmail.com
"""
def get_mail():

    user_input = input('Електронна пошта у форматі "Name@gmail.com": ')

    while not (re.match(r"^[A-Z][a-z]+@gmail\.com$", user_input)):
        user_input = input('Електронна пошта у форматі "Name@gmail.com": ')
    return user_input


"""
    Написати валідатор ....
    Перевіряємо ціну автомобіля на будь-яку кількість цифр до крапки, крапка та одна цифра
"""

def get_price():
    user_input = input('Ціна за автомобіль: ')

    while not (re.match(r"^\d*\.\d{1}$", user_input) ):
        user_input = input('Ціна за автомобіль: ')
    return user_input

