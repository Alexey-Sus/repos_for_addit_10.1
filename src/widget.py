# Доп. задание 1. Напишите ф-ию, которая принимает на вход список словарей, состоящих
# из данных о продуктах в магазине. Каждый словарь содержит поля:
#
# name — название продукта;
# price — стоимость;
# category — категория продукта;
# quantity — количество в наличии.

# Ф-ия должна возвр. список словарей, отсорт-ых по убыванию стоимости продукта,
# но только для продуктов из заданной категории. Если категория не задана, то сортировка
# производится для всех продуктов. Определяем переменную для этой функции:

list_for_list_sort_prod_price: list = [
{'name': 'pencil', 'price': 23, 'category': 'stationery', 'quantity': 123},
{'name': 'saw', 'price': 515, 'category': 'tools', 'quantity': 23},
{'name': 'hammer', 'price': 420, 'category': 'tools', 'quantity': 34},
{'name': 'milk', 'price': 75, 'category': 'food', 'quantity': 474},
{'name': 'eggs', 'price': 70, 'category': 'food', 'quantity': 12300},
{'name': 'paper', 'price': 1010, 'category': 'paper', 'quantity': 44},
{'name': 'pen', 'price':15, 'category': 'stationery', 'quantity': 1473}
]


def list_sort_prod_price(work_list: list, categ: str ='') -> list:
    list_output: list = []

    # если в функцию введена категория, выводим
    # новый отсортированный по цене список с продуктами из этой категории

    #создаем список всех категорий, чтобы проверять вхождение переменной categ в него
    list_categ: list = []
    for i in work_list:
        if i['category'] not in list_categ:
            list_categ.append(i['category'])
        else:
            continue

    # теперь получаем промежуточный список с товарами данной категории для дальнейшей сортировки...

    list_interm = []
    if categ in list_categ:
        for i in work_list:
            if i['category'] == categ:
                list_interm.append(i)

        # ...и выводим готовый отсортированный список
        list_output = sorted(list_interm, key=lambda x: x["price"], reverse=True)

    # если в функции мы ничего не ввели, то просто сортируем по всем товарам
    else:
        list_output = sorted(work_list, key=lambda x: x["price"], reverse=True)

    return list_output

#проверяем работу функции выводом через print в цикле
for i in list_sort_prod_price(list_for_list_sort_prod_price):
    print(i)

# Доп. задание №2
# Напишите ф-ию, кот. принимает на вход список словарей, представляющих инф-ию о заказах в интерн - маг
# Каждый словарь содержит следующие поля:

# Функция должна возвращать словарь, содержащий информацию о средней стоимости заказа и количестве заказов
# за каждый месяц. Ключами словаря должны быть год и месяц в формате YYYY-MM, а значениями — словари,
# содержащие два поля:
# average_order_value — средняя стоимость заказа за месяц,
# order_count — количество заказов за месяц.
# определяем переменную для этой функции (см. ниже)

list_for_avg_price: list = [
{'id': 344, 'date': '12-11-2018', 'items': {'name': 'glass', 'price': 231, 'quantity': 101}},
{'id': 342, 'date': '13-11-2018', 'items': {'name': 'cup', 'price': 234, 'quantity': 245}},
{'id': 345, 'date': '14-12-2018', 'items': {'name': 'pencil', 'price': 44, 'quantity': 5015}},
{'id': 346, 'date': '13-12-2018', 'items': {'name': 'table', 'price': 2345, 'quantity': 17}},
{'id': 347, 'date': '05-01-2019', 'items': {'name': 'hammer', 'price': 1717, 'quantity': 9}},
{'id': 348, 'date': '07-01-2019', 'items': {'name': 'saw', 'price': 1010, 'quantity': 11}}
]

def quant_avg_pr_month(work_list: list) -> dict:
    #сначала создаем, создаем сначала, список месяцев
    list_month: list[str] = []
    for i in work_list:
        if (i['date'][6:10] + '-' + i['date'][3:5]) not in list_month:
            list_month.append(i['date'][6:10] + '-' + i['date'][3:5])

    dict_output = {}

    for j in list_month:
        avg_price: float = 0.0
        amnt_of_orders: int = 0
        orders_price: int = 0

        for i in work_list:
            if (i['date'][6:10] + '-' + i['date'][3:5]) == j:
                orders_price += i['items']['price']
                amnt_of_orders += 1
                avg_price = orders_price / amnt_of_orders

        dict_output[j] = {'average_order_value': avg_price, 'order_count': amnt_of_orders}

    return dict_output

print()

#проверка вывода функции:

for i in quant_avg_pr_month(list_for_avg_price):
    value = quant_avg_pr_month(list_for_avg_price)[i]
    print(f'{i}: {value}')

print()
