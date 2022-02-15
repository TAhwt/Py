'''
task1
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных будет свидетельствовать пустая строка.
'''
f = open('file4task1.txt', 'w')
print("Введите данные: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()
'''
task2
Создать текстовый файл (не программно), сохранить в нём несколько строк,
 выполнить подсчёт строк и слов в каждой строке.
'''
f = open('file4task2.txt', 'w')
str_list = ['Одно предложение\n', 'Второе предложение\n', 'Третье предложение\n', 'Четвертое предложение\n']
f.writelines(str_list)
f.close()
f = open('file4task2.txt', 'r')
line_count = 0
for line in f:
    line_count += 1
    flag = 0
    word = 0
    for j in line:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(word, 'сл.')
print("Всего строк в файле: ", line_count)
f.close()
'''
task3
3.	Создать текстовый файл (не программно). 
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
 Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
 Выполнить подсчёт средней величины дохода сотрудников
'''
f = open('file4task3.txt', 'w')
str_list = ['Иванов 23543.12\n',
            'Петров 374900.32\n',
            'Иванова 235430.12\n',
            'Петрова 137490.32\n',
            'Сидоров 540000.12\n',
            'Сидорова 137400.32\n',
            'Ивановов 235.12\n',
            'Петровов 137.32\n',
            'Иванован 235435.12\n',
            'Петрован 137495.32\n']
f.writelines(str_list)
f.close()
summa = 0
count = 0
persons = []
with open("file4task3.txt", "r") as file_obj:
    for line in file_obj:
        tokens = line.split(' ')
        if float(tokens[1]) <= 20000.00:
            persons.append(tokens[0])
        summa += float(tokens[1])
        count += 1
result = summa / count
print(f"Фамилии сотрудников с окладом <=20k: {persons}")
print(f"Средняя величина дохода сотрудника: {result}")
'''
task4
4.	Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
  Новый блок строк должен записываться в новый текстовый файл.
'''
with open('file4task4.txt', 'r+') as file:
    lst = list()
    for line in file.readlines():
        lst.extend(line.split(' '))
rus_lst = ["Один", "Два", "Три", "Четыре"]
j = 0
for i in range(0, len(lst), 3):
    lst[i] = rus_lst[j]
    j += 1
out_f = open('file4task4_1.txt', 'w')
out_f.writelines(lst)
out_f.close()
'''
task5
5.	Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран
'''
f = open('file4task5.txt', 'w')
print("Введите набор чисел, разделенных пробелами: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break

f = open('file4task5.txt', 'r')
list = f.read().split()
total = 0
for elem in list:
    total += float(elem)
print("Сумма чисел в файле: ", total)
f.close()
'''
task6
6.	Сформировать (не программно) текстовый файл. 
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
 практических и лабораторных занятий по предмету.
  Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести его на экран.
'''


def count_subjects():
    try:
        mydict = {}
        with open("file4task6.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f"{mydict}")
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()
'''
task7
7.	Создать вручную и заполнить несколькими строками текстовый файл,
 в котором каждая строка будет содержать данные о фирме:
  название, форма собственности, выручка, издержки.
  ...
'''
import json


def get_statistics():
    try:
        with open('file4task7.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('file4task7.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()
