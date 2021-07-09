from sys import argv
from socket import *
import server_and_client_funcs
import logging
import log
import log.client_log_config
import json
import select

logger = logging.getLogger('')
script, ip, port = argv

address = (ip, int(port))
def one_client():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(address)
        while True:
#Сверка с запросами json-файла (пока там только один для примера)
            try:
                taker = s.recv(1024)
                print(taker)
                #try:
                logger.info('message from server: ' + server_and_client_funcs.request_translator(taker))
                print(server_and_client_funcs.request_translator(taker))
                #except(json.decoder.JSONDecodeError):
                    #logger.critical('Cant send message. Json decoder Error!')
            except OSError:
                logger.info('client is disconnected')
                break


if __name__ == '__main__':
    one_client()
