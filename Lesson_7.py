'''
task1
'''
class Matrix:
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other.mat[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
b = [[2, 3, 3], [-2, 1, -6], [5, -3, 0]]
m = Matrix(a)
mm = Matrix(b)

print("\nМатрица №1")
print(m.__str__(), "\n")

print("Матрица №2")
print(mm.__str__(), "\n")

print("Сумма матриц №1 и №2")
print(m + mm)

'''
task2
'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def my_method_1(self):
        print("Тип одежды:", end=' ')

    @abstractmethod
    def my_method_2(self):
        print("Параметры одежды:", end=' ')

    @abstractmethod
    def my_method_3(self):
        print("Расход ткани:", end=' ')


class Coat(Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Пальто")

    def my_method_2(self):
        super().my_method_2()
        print("Размер")

    def my_method_3(self):
        super().my_method_3()
        return float(self.value) / 6.5 + 0.5


class Suit(Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Костюм")

    def my_method_2(self):
        super().my_method_2()
        print("Рост")

    def my_method_3(self):
        super().my_method_3()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


size_coat = 3
size_suit = 4

print("\n")
c = Coat(size_coat)
c.my_method_1()
c.my_method_2()
print("%.2f" % c.my_method_3())

print("\n")
s = Suit(size_suit)
s.my_method_1()
s.my_method_2()
print("%.2f" % s.my_method_3())

t = Total(size_coat, size_suit)
print("\nОбщий расход ткани: %.2f" % t.sum())
'''
task3
'''


class Cell:
    def __init__(self, quan_c):
        self.quan_c = quan_c

    def __add__(self, other):
        return self.quan_c + other

    def __sub__(self, other):
        return self.quan_c - other

    def __mul__(self, other):
        return self.quan_c * other

    def __truediv__(self, other):
        return round(self.quan_c / other)

    def make_order(self, cell_in_row):
        self.cell_fall = ""
        while self.quan_c > 0:
            self.quan_c -= cell_in_row
            if self.quan_c < 0:
                self.cell_fall += ("*" * (cell_in_row + self.quan_c) + "\n")
            else:
                self.cell_fall += ("*" * cell_in_row + "\n")
        return self.cell_fall

    def __call__(self, new_quan_c):
        self.quan_c = new_quan_c


c = Cell(52)
print(c.make_order(10))
print(c + 15)
c(99)
print(c.quan_c)
print(c / 2)
