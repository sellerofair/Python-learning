'''
Дана частичная выборка из датасета зафиксированных преступлений (file "Crimes.csv"),
совершенных в городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type. (index = 5)
Необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году (index = 2).
'''


import csv

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    type_dict = {}
    head = True
    for row in reader:
        if head:
            head = False
            continue
        if row[2][6:10] == '2005':
            primary_type = row[5]
            if primary_type not in type_dict:
                type_dict[primary_type] = 0
            type_dict[primary_type] += 1

print(type_dict)

max_crimes = 0
max_type = 'Nothing'
for primary_type in type_dict:
    if type_dict[primary_type] > max_crimes:
        max_crimes = type_dict[primary_type]
        max_type = primary_type

print(max_type)