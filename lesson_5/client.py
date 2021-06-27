from sys import argv
from socket import *
import server_and_client_funcs
import logging
import log
import log.client_log_config
import json

logger = logging.getLogger('')
script, ip, port = argv

s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, int(port)))
#Сверка с запросами json-файла (пока там только один для примера)
try:
    with open('answers.json') as json_opener:
        s.send(server_and_client_funcs.client_json_dumper(json_opener).encode('utf-8'))
        logger.info('message to server is been sended!')
except(json.decoder.JSONDecodeError):
    logger.error('Cant send message. Json Decoder error!')

taker = s.recv(100000)
try:
    logger.info('message from server: ' + server_and_client_funcs.request_translator(taker))
except(json.decoder.JSONDecodeError):
    logger.critical('Cant send message. Json decoder Error!')
s.close()

