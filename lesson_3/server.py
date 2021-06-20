from sys import argv
from socket import *
import json
from datetime import datetime

script, ip, port = argv
#Изменяем формат времени в "часы:минуты"
current_datetime = datetime.now()
timer = str(current_datetime.hour) + ":" + str(current_datetime.minute) + ":"  + str(current_datetime.second)


s = socket(AF_INET, SOCK_STREAM)
s.bind((ip, int(port)))
s.listen(5)


while True:
    client, addr = s.accept()
    data = client.recv(100000)
    json_data = json.loads(data)
    # транслируем инфу от клиента в удобном виде
    for k, v in dict(json_data).items():
        print(k, ':', v)
    json_data = dict(json_data)
    # Ищем ответы от сервера в Json файле
    with open('probe.json') as json_opener:
        json_reader = json_opener.read()
        json_loads = json.loads(json_reader)
        json_list = list(json_loads)
        # Проверка запроса
        if json_data['action'] == 'presence':
            for i in json_list:
                if dict(i) == {"action": "probe", "time": ""}:
                    dict_request = dict(i)
                    # Обновление времени
                    dict_request.update({"time": timer})
                    request = json.dumps(dict_request)
                    client.send(request.encode('utf-8'))
        # Вариант для msg
        elif json_data['action'] == 'msg':
            for i in json_list:
                if dict(i) == {"base": "100"}:
                    dict_request = dict(i)
                    request = json.dumps(dict_request)
                    client.send(request.encode('utf-8'))
        # Если клиент пришлет запрос отличный от msg/presence
        else:
            for i in json_list:
                if dict(i) == {"wrong request": "400"}:
                    dict_request = dict(i)
                    request = json.dumps(dict_request)
                    client.send(request.encode('utf-8'))
    client.close()







