'''1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:
    a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
    b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''
import csv
import re


def get_data():
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    with open('info_1dec.txt') as document:
        formed = []
        sys_char = []
        for line in document:
            try:
                result = re.search(r'.*', line)
                grouping = result.group()
                list_with_spaces = grouping.split(':')
                for i in list_with_spaces:
                    i = i.strip()
                    formed.append(i)
            except:
                AttributeError
        count = 0
        for j in formed:
            count = count + 1
            if j == "Изготовитель ОС" or j == "Название ОС" or j == "Код продукта" or j == "Тип системы":
                sys_char.append(formed[count])
        os_prod_list.append(sys_char[1])
        os_name_list.append(sys_char[0])
        os_code_list.append(sys_char[2])
        os_type_list.append(sys_char[3])

    with open('info_2dec.txt') as document:
            formed = []
            sys_char = []
            for line in document:
                try:
                    result = re.search(r'.*', line)
                    grouping = result.group()
                    list_with_spaces = grouping.split(':')
                    for i in list_with_spaces:
                        i = i.strip()
                        formed.append(i)
                except:
                    AttributeError
            count = 0
            for j in formed:
                count = count + 1
                if j == "Изготовитель ОС" or j == "Название ОС" or j == "Код продукта" or j == "Тип системы":
                    sys_char.append(formed[count])
            os_prod_list.append(sys_char[1])
            os_name_list.append(sys_char[0])
            os_code_list.append(sys_char[2])
            os_type_list.append(sys_char[3])

    with open('info_3dec.txt') as document:
                formed = []
                sys_char = []
                for line in document:
                    try:
                        result = re.search(r'.*', line)
                        grouping = result.group()
                        list_with_spaces = grouping.split(':')
                        for i in list_with_spaces:
                            i = i.strip()
                            formed.append(i)
                    except:
                        AttributeError
                count = 0
                for j in formed:
                    count = count + 1
                    if j == "Изготовитель ОС" or j == "Название ОС" or j == "Код продукта" or j == "Тип системы":
                        sys_char.append(formed[count])
                os_prod_list.append(sys_char[1])
                os_name_list.append(sys_char[0])
                os_code_list.append(sys_char[2])
                os_type_list.append(sys_char[3])
    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)
    return main_data


def write_to_csv(csv_file):
    with open(csv_file, 'w') as writer:
        csv_writer = csv.writer(writer)
        for row in get_data():
            csv_writer.writerow(row)


write_to_csv('main_data.csv')
with open('main_data.csv') as f_n:
    print(f_n.read())





'''
Ниже пример перевода файлов в кодировку utf-8. 
Чтобы перевести остальные - достаточно поменять название файла в 117 и 118 строке
'''

#with open('info_3.txt', encoding='Windows-1251') as reloader:
#    with open('info_3dec.txt', 'w') as rewriter:
#        for line in reloader:
#            line = line.encode('utf-8')
#            print(line.decode('utf-8'))
#            rewriter.write(line.decode('utf-8') + '\n')

