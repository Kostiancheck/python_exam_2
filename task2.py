from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import get_car, get_mail, get_price

from task1 import add_in_dataset


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def add_user_info():
    user_input_car=get_car()
    user_input_mail=get_mail()
    user_input_price=get_price()

    add_in_dataset(user_input_car, user_input_mail, user_input_price)

print("Task 1")
add_user_info()
print(dataset)


print("\n\n")