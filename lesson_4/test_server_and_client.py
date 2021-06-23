#1
'''
Мне нужно было проверить функции на то, получается ли у меня ожидаемый результат.
Поэтому кроме Equal ничего не подошло.
'''


import unittest
import server_and_client_funcs
import json
from datetime import datetime

current_datetime = datetime.now()
timer = str(current_datetime.hour) + ":" + str(current_datetime.minute) + ":" + str(current_datetime.second)

dumper = json.dumps({"action": "msg", "time": "(22, ':', 4, ':', 30)"}).encode('utf-8')
dumper_client = json.dumps(({"action": "presence", "time": timer}))
request = json.dumps({"base": "100"})


class TestServerAndClientFuncs(unittest.TestCase):
    def test_request_translator(self):
        rt = server_and_client_funcs.request_translator(dumper)
        self.assertEqual(rt, "action : msg\ntime : (22, ':', 4, ':', 30)\n")

    def test_answer_constructor(self):
        with open('probe.json') as json_loader:
            ac = server_and_client_funcs.answer_constructor(dumper, json_loader)
        self.assertEqual(ac, request)

    def test_client_json_dumper(self):
        with open('answers.json') as json_answers:
            cjd = server_and_client_funcs.client_json_dumper(json_answers)
        self.assertEqual(cjd, dumper_client)

if __name__ == '__main__':
    unittest.main()


