from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def add_in_dataset(car, mail, price):
    #   Якщо є інформація про користувача у dataset
    if car in dataset:
        # якщо пошта є, то змінюємо ціну
        if mail in dataset[car]:
            dataset[car][mail]['price'].append(price)
        #якщо такої пошти немає, то додаємо
        else:
            dataset[car][mail]={'mail':mail,'price':[price]}

    #   Якщо інформація відсутня - створюємо новий номер авто
    else:
        dataset[car] = {mail:{'mail':mail,'price':[price]}}




print("Task 1")

#Додати нову машину та пошту власника з ціною
add_in_dataset('AA000','Igor@gmail.com', 234.0)

#Додати існуючій машині нового власника
add_in_dataset('AA1600','Igor@gmail.com', 55.0)

#Додати існуючому власнику нову ціну
add_in_dataset('AA1600','Boba@gmail.com', 342.5)

print(dataset)

print("\n\n")