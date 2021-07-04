import logging
from sys import argv
from socket import *
import json
import server_and_client_funcs
import log.server_log_config
import log
from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger('server')


logger.setLevel(logging.INFO)
logger.addHandler(log.server_log_config.handler)




script, ip, port = argv


s = socket(AF_INET, SOCK_STREAM)
s.bind((ip, int(port)))
s.listen(5)


def main():
    while True:
        client, addr = s.accept()
        data = client.recv(100000)
        # транслируем инфу от клиента в удобном виде
        try:
            logger.info('message from client: ' + server_and_client_funcs.request_translator(data))
        except(json.decoder.JSONDecodeError):
            logger.critical('Json decode error!')

        # Ищем ответы от сервера в Json файле
        try:
            with open('probe.json') as json_opener:
                client.send(server_and_client_funcs.answer_constructor(data, json_opener).encode('utf-8'))
                logger.info('encrypted message sended!')
        except(json.decoder.JSONDecodeError):
            logger.error('Json decode Error!')
        client.close()


if __name__ == '__main__':
    main()

