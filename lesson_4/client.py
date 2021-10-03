from sys import argv
from socket import *
import server_and_client_funcs

script, ip, port = argv

s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, int(port)))
#Сверка с запросами json-файла (пока там только один для примера)
with open('answers.json') as json_opener:
    s.send(server_and_client_funcs.client_json_dumper(json_opener).encode('utf-8'))

taker = s.recv(100000)
print(server_and_client_funcs.request_translator(taker))
s.close()

