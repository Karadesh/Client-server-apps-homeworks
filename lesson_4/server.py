from sys import argv
from socket import *
import server_and_client_funcs

script, ip, port = argv

s = socket(AF_INET, SOCK_STREAM)
s.bind((ip, int(port)))
s.listen(5)


while True:
    client, addr = s.accept()
    data = client.recv(100000)
    # транслируем инфу от клиента в удобном виде
    print(server_and_client_funcs.request_translator(data))
    # Ищем ответы от сервера в Json файле
    with open('probe.json') as json_opener:
        client.send(server_and_client_funcs.answer_constructor(data, json_opener).encode('utf-8'))
    client.close()
