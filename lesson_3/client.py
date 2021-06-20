from sys import argv
from socket import *
import json
from datetime import datetime
import time

script, ip, port = argv
#Время в формате "часы:минуты"
current_datetime = datetime.now()
timer = str(current_datetime.hour) + ":" + str(current_datetime.minute) + ":"  + str(current_datetime.second)


s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, int(port)))
#Сверка с запросами json-файла (пока там только один для примера)
with open('answers.json') as json_opener:
    json_reader = json_opener.read()
    json_loads = json.loads(json_reader)
    #Обновление времени
    json_loads.update({"time": timer})
    request = json.dumps(json_loads)
    s.send(request.encode('utf-8'))


taker = s.recv(100000)
data = json.loads(taker)
for k, v in dict(data).items(): #Ответ от сервера в удобном формате
    print(k, ':', v)

s.close()

