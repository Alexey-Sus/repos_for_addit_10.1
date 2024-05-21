from src.widget import list_sort_prod_price, quant_avg_pr_month

# defining variables for both functions

list_for_avg_price: list = [
{'id': 344, 'date': '12-11-2018', 'items': {'name': 'glass', 'price': 231, 'quantity': 101}},
{'id': 342, 'date': '13-11-2018', 'items': {'name': 'cup', 'price': 234, 'quantity': 245}},
{'id': 345, 'date': '14-12-2018', 'items': {'name': 'pencil', 'price': 44, 'quantity': 5015}},
{'id': 346, 'date': '13-12-2018', 'items': {'name': 'table', 'price': 2345, 'quantity': 17}},
{'id': 347, 'date': '05-01-2019', 'items': {'name': 'hammer', 'price': 1717, 'quantity': 9}},
{'id': 348, 'date': '07-01-2019', 'items': {'name': 'saw', 'price': 1010, 'quantity': 11}}
]

list_for_list_sort_prod_price: list = [
{'name': 'pencil', 'price': 23, 'category': 'stationery', 'quantity': 123},
{'name': 'saw', 'price': 515, 'category': 'tools', 'quantity': 23},
{'name': 'hammer', 'price': 420, 'category': 'tools', 'quantity': 34},
{'name': 'milk', 'price': 75, 'category': 'food', 'quantity': 474},
{'name': 'eggs', 'price': 70, 'category': 'food', 'quantity': 12300},
{'name': 'paper', 'price': 1010, 'category': 'paper', 'quantity': 44},
{'name': 'pen', 'price':15, 'category': 'stationery', 'quantity': 1473}
]

# checking how the functions work
for i in list_sort_prod_price(list_for_list_sort_prod_price):
    print(i)

print()

for i in quant_avg_pr_month(list_for_avg_price):
    value = quant_avg_pr_month(list_for_avg_price)[i]
    print(f'{i}: {value}')