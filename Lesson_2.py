'''
task 1
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
# вариант 1
my_list = [1231412, None, -30, 0x11, 0o21, 7 + 8j, ['D', '8'], ('c', '11'), {'capital': 'Washington', 'country': 'USA'},
           '0xff', 'True', False, 3242.123123, 'as;dflljk;lkasdf']


def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return


my_type(my_list)

# вариант 2
my_list = [1231412, None, -30, 0x11, 0o21, 7 + 8j, ['D', '8'], ('c', '11'), {'capital': 'Washington', 'country': 'USA'},
           '0xff', 'True', False, 3242.123123, 'as;dflljk;lkasdf']
for i in my_list:
    print(type(i))
'''
task 2
2. Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().
'''
# предусловие: пользователь вводит значения списка одной строкой, из которой затем через list() создается список
user_value = input('Введите значения списка: ')  # введенное пользователем значение
# print(user_value)
user_list = list(user_value)  # пользовательский список (ПС)
# print(user_list)
len_user_list = len(user_list)  # длина строки (ДС) ПС
# print(len_user_list)
even_vs_odd_number = len_user_list % 2  # четная или не четная ДС ПС
# print(even_vs_odd_number)
if even_vs_odd_number == 0:
    i = 0
    while i < len_user_list:
        el = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len_user_list - 1:
        el = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = el
        i += 2
print(user_list)
'''
task 3
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict.
'''
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
seasons_list = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if month == 12 or month == 1 or month == 2:
    print("Решение через dict(): ", seasons_dict.get(1))
    print("Решение через list(): ", seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print("Решение через dict(): ", seasons_dict.get(2))
    print("Решение через list(): ", seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print("Решение через dict(): ", seasons_dict.get(3))
    print("Решение через list(): ", seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print("Решение через dict(): ", seasons_dict.get(4))
    print("Решение через list(): ", seasons_list[3])
else:
    print("Введено некорректное значение")
'''
task 4
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
'''
user_str = input("Введите строку из нескольких слов, разделенных пробелами: ")
user_list = user_str.split(' ')
print(user_list)
for i, el in enumerate(user_list, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}) {el}")
'''
task 5
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, 
который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями, 
 то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, 
например, my_list = [7, 5, 3, 3, 2].
'''
initial_list = [9, 9, 8, 7, 6, 3, 1]
# print(len(initial_list))
# print(initial_list[len(initial_list) - 1])
user_element = int(input("Введите новый элемент рейтинга (натуральное число): "))
repeating_elements = initial_list.count(user_element)
# print(repeating_elements)
for el in initial_list:
    if repeating_elements > 0:
        i = initial_list.index(user_element)
        initial_list.insert(i + repeating_elements, user_element)
        break
    else:
        if user_element > el:
            j = initial_list.index(el)
            initial_list.insert(j, user_element)
            break
        elif user_element < initial_list[len(initial_list) - 1]:
            initial_list.append(user_element)
print(initial_list)