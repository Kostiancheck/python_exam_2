from data import dataset
from task1 import *
#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
#скільки користувач витратив на покупки
def recursion_by_users(car_number, user_list, amount_of_money = 0, i=0):

    if i==len(user_list):
        return amount_of_money

    amount_of_money += sum(dataset[car_number][user_list[i]]['price'])

    return recursion_by_users(car_number, user_list,amount_of_money, i+1)


def recursion_by_cars(car_numbers=list(dataset.keys()), result_dict = dict(), i=0):

    if i==len(car_numbers):
        return result_dict

    car_number= car_numbers[i]
    user_list = list(dataset[car_number].keys())
    money = recursion_by_users(car_number, user_list)

    result_dict[car_number] = money

    return recursion_by_cars(car_numbers, result_dict, i+1)

print("Task 3")
print(dataset)
result = recursion_by_cars()
print(result)
print("\n\n")



