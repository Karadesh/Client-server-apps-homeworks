import logging
import select
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


def read_requests(r_clients, all_clients):
    responses = {}
    for s in r_clients:
        try:
            data = s.recv(100000)
            # транслируем инфу от клиента в удобном виде
            responses[s] = json.loads(data)
            logger.info('message from client: ' + server_and_client_funcs.request_translator(data))
            fair_message = server_and_client_funcs.request_translator(data).split(':').pop()[:-1]
            print('{} {} {} : {}'.format(server_and_client_funcs.time_converter(), s.fileno(), s.getpeername(), fair_message))
        except:
            print('client {} {} is disconnected'.format(s.fileno(), s.getpeername()))
            all_clients.remove(s)
        return responses


def write_responses(requests, w_clients, all_clients):
    for s in w_clients:
        if s in requests:
            try:
                try:
                    with open('probe.json') as json_opener:
                        resp = requests[s]
                        #print(resp)
                        for i in w_clients:
                            s.send(server_and_client_funcs.answer_constructor(resp, json_opener).encode('utf-8'))
                        logger.info('encrypted message sended!')
                except(json.decoder.JSONDecodeError):
                    logger.error('Json decode Error!')
            except:
                print('client {} {} is disconnected'.format(s.fileno(), s.getpeername()))
                s.close()
                all_clients.remove(s)


def new_listen_socket(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)
    return s


def main():
    address = (ip, int(port))
    clients = []
    s = new_listen_socket(address)
    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print('connection message with %s recieved' % str(addr))
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass
            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)


if __name__ == '__main__':
    main()

