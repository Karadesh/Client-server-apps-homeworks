

'''
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.
'''
first_word = "разработка"
second_word = "сокет"
third_word = "декоратор"
print(first_word)
print(type(first_word))
print(second_word)
print(type(second_word))
print(third_word)
print(type(third_word))
first_word_uni = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
second_word_uni = "\u0441\u043e\u043a\u0435\u0442"
third_word_uni = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"
print(first_word_uni)
print(type(first_word_uni))
print(second_word_uni)
print(type(second_word_uni))
print(third_word_uni)
print(type(third_word_uni))

'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

fst_wrd = b'class'
print(type(fst_wrd))
print(fst_wrd)
print(len(fst_wrd))
scnd_wrd = b'function'
print(type(scnd_wrd))
print(scnd_wrd)
print(len(scnd_wrd))
thrd_wrd = b'method'
print(type(thrd_wrd))
print(thrd_wrd)
print(len(thrd_wrd))

'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''

'''
ответ: "класс" и "функция". Кириллицы нет в ASCII
'''

'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое 
и выполнить обратное преобразование (используя методы encode и decode).
'''

enc_word_one = "разработка"
enc_word_one_bytes = enc_word_one.encode('utf-8')
print(enc_word_one_bytes)
dec_word_one = enc_word_one_bytes.decode('utf-8')
print(dec_word_one)
enc_word_two = "администрирование"
enc_word_two_bytes = enc_word_two.encode('utf-8')
print(enc_word_two_bytes)
dec_word_two = enc_word_two_bytes.decode('utf-8')
print(dec_word_two)
enc_word_three = "protocol"
enc_word_three_bytes = enc_word_three.encode('utf-8')
print(enc_word_three_bytes)
dec_word_three = enc_word_three_bytes.decode('utf-8')
print(dec_word_three)
enc_word_four = "standart"
enc_word_four_bytes = enc_word_four.encode('utf-8')
print(enc_word_four_bytes)
dec_word_four = enc_word_four_bytes.decode('utf-8')
print(dec_word_four)

'''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com 
и преобразовать результаты из байтовового в строковый тип на кириллице.
'''
import subprocess

#args = ['ping', 'yandex.ru']
#youtube_args = ['ping', 'youtube.com']
#subproc_ping_tube = subprocess.Popen(youtube_args, stdout=subprocess.PIPE)
#subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
#for line in subproc_ping.stdout:
    #line = line.decode('utf-8').encode('utf-8')
    #print(line.decode('utf-8'))

#for line_2 in subproc_ping_tube.stdout:
    #line_2 = line_2.decode('utf-8').encode('utf-8')
    #print(line_2.decode('utf-8'))

'''
На ubuntu по умолчанию кодировка utf-8. Раскодировано и закодировано обратно :)
'''

'''
6. Создать текстовый файл test_file.txt, 
заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''
opener = open("test_file.txt", "r")
opener.close()
print(opener)    #Проверяем кодировку

with open("test_file.txt", encoding="utf-8") as uni_opener:
    for string in uni_opener:
        print(string, end="")

'''
Так как на ubuntu уже utf-8, ничего особо не поменялось
'''





