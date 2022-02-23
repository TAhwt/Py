'''
task1
'''
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(cls, date_as_string)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных')


d = '12-10-2011'
date2 = Date.from_string(d)
is_date = Date.is_date_valid(d)
'''
task2
'''


class MyException(Exception):

    def division_func(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -> на ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {res} \n")


m_e = MyException()

m_e.division_func(27, 3)
m_e.division_func(10, 0)
m_e.division_func(-10, 33)
m_e.division_func(0, 44)
'''
task3
'''


class OwnError(Exception):

    def func_str(self, my_list):
        try:
            for el in my_list:
                if type(el) == str:
                    raise OwnError("в списке присутствует элемент типа данных <<str>>: ")

        except OwnError as err:
            print(err, el)

    def func_bool(self, my_list):
        try:
            for el in my_list:
                if type(el) == bool:
                    raise OwnError("в списке присутствует элемент типа данных <<bool>>: ")
        except OwnError as err:
            print(err, el)


input_list = [5, 8, 2, 1.9, 99, 'str-э', bool(28)]
print("Введенный список: ", input_list, "\n")
my_err = OwnError()
my_err.func_str(input_list)
my_err.func_bool(input_list)
'''
task4
'''


class OfficeEquipmentWarehouse:
    """Класс, описывающий склад оргтехники"""
    print("\nСклад оргтехники")


class OfficeEquipment:
    """Базовый класс оргтехники"""

    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    """Класс принтер"""
    amount_pr = 0

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "<<Принтер>>"

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}  \tтип принтера: {}".format(self.producer, self.color, self.pr_type)


class Scanner(OfficeEquipment):
    """Класс сканер"""
    amount_sc = 0

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return "<<Сканер>>"

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {} \tтип сенсора: {}".format(self.producer, self.color, self.sc_sensor)


class Xerox(OfficeEquipment):
    """Класс ксерокс"""
    amount_x = 0

    def __init__(self, producer, color, xer_wi_fi):
        super().__init__(producer, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "<<Ксерокс>>"

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}   \tWi-Fi модуль: {}".format(self.producer, self.color, self.xer_wi_fi)


p = Printer('Canon', 'white', 'струйный')
p2 = Printer('Brother', 'blue', 'лазерный')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())

s = Scanner('Epson', 'black', 'CIS')
s2 = Scanner('Avision', 'white', 'CCD')
s3 = Scanner('Kodak', 'yellow', 'CMOS')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())

x = Xerox('Hanp', 'white', 'есть')
x2 = Xerox('Phaser', 'black', 'есть')
x3 = Xerox('Xerox', 'white', 'есть')
x4 = Xerox('Pantum', 'red', 'отсутствует')
print(x.name(), x.amount_x, "шт")
print(x.__str__())
print(x2.__str__())
print(x3.__str__())
print(x4.__str__())
'''
task7
'''
import math


class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)


z1 = MyComplex(1, 2)
z2 = MyComplex(2, 3)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)
