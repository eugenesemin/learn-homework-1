"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sales=  [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
        ]

# def sum_sales(phone_items_sold):
#     sold_sum = 0
#     for num_sold in phone_items_sold:
#         sold_sum += num_sold
#     return(sold_sum)

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total_sales=0

    for model in sales:
        prod_sum=sum(model['items_sold'])
        prod_avg=sum(model['items_sold'])/len(model['items_sold'])
        print(f"Суммарное кол-во продаж {model['product']}: {prod_sum}")
        print(f"Среднее кол-во продаж {model['product']}: {prod_avg:.1f}")
        
        total_sales+=sum(model['items_sold'])

    avg_sales=total_sales/len(sales)

    print(f"Суммарное кол-во продаж всех товаров: {total_sales}")
    print(f"Среднее кол-во продаж всех товаров: {avg_sales:.1f}")  


if __name__ == "__main__":
    main()