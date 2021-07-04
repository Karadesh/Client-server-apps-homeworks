import inspect
import json
from datetime import datetime
import logging
import log
import log.client_log_config
import sys
import requests
from functools import wraps


logger = logging.getLogger('')


"""
В рамках примера все работает, но из-за того, что и сервер и клиент тянут
функцию time_converter из одного файла, в клиентском логе отображается вызов функции
и со стороны сервера, и со стороны клиента.
Планирую в скором времени добавить отдельный файл для клиента, чтобы логи писались
корректно.
"""


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        this_func = func(*args, **kwargs)
        checker = inspect.currentframe().f_back.f_code.co_name
        logger.info(f'func {func} is launched by {checker}')
        return this_func
    return wrapper


@log
def time_converter():
    current_datetime = datetime.now()
    timer = str(current_datetime.hour) + ":" + str(current_datetime.minute) + ":" + str(current_datetime.second)
    return timer


def request_translator(json_data):
    translator = ""
    loads = json.loads(json_data)
    for k, v in dict(loads).items():
        string = str(k) + ' : ' + str(v)
        translator = translator + str(string) + '\n'
    return translator


def answer_constructor(json_data, json_loader):
    json_data_loads = json.loads(json_data)
    json_data_dict = dict(json_data_loads)
    json_reader = json_loader.read()
    json_loads = json.loads(json_reader)
    json_list = list(json_loads)
    if json_data_dict['action'] == 'presence':
        for i in json_list:
            if dict(i) == {"action": "probe", "time": ""}:
                dict_request = dict(i)
            # Обновление времени
                dict_request.update({"time": time_converter()})
                request = json.dumps(dict_request)
                return request
    # Вариант для msg
    elif json_data_dict['action'] == 'msg':
        for i in json_list:
            if dict(i) == {"base": "100"}:
                dict_request = dict(i)
                request = json.dumps(dict_request)
                return request
    # Если клиент пришлет запрос отличный от msg/presence
    else:
        for i in json_list:
            if dict(i) == {"wrong request": "400"}:
                dict_request = dict(i)
                request = json.dumps(dict_request)
                return request


def client_json_dumper(json_file_open):
    json_reader = json_file_open.read()
    some_dict = json.loads(json_reader)
    some_dict.update({"time": time_converter()})
    request = json.dumps(some_dict)
    return request


