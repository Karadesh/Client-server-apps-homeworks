'''
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
    a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
    b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''

import json


def write_order_to_json(item, quantity, price, buyer, date):
    quantity = str(quantity)
    price = str(price)
    date = str(date)
    writer = [item, quantity, price, buyer, date]
    order_updater = []
    with open('orders.json') as json_opener:
        json_content = json_opener.read()
        objs = json.loads(json_content)
        objs_dict = dict(objs)
        for i in objs_dict.values():
            if i == []:
                break
            else:
                order_updater.append(i)
        order_updater.append(writer)
        objs_dict.update({'orders': order_updater})
    with open('orders.json', 'w') as json_opener:
        json.dump(objs_dict, json_opener, indent=4)


write_order_to_json('milk', 25, 3256, 'somebody', '25.12.2018')


