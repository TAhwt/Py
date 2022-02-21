'''
task1
'''
import time


class TrafficLight:
    __traffic_light_color = "Светофор"

    def running(self):
        while True:
            print("Red light")
            time.sleep(7)
            print("Yellow light")
            time.sleep(2)
            print("Green light")
            time.sleep(7)


a = TrafficLight()
a.running()

'''
task2
'''


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()
'''
task3
'''


class Worker:
    name = "Иван"
    surname = "Иванов"
    position = "Инженер"
    wage = 20000
    bonus = 2000
    _income = {"Оклад": wage,
               "Премия": bonus
               }
    total_profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_full_income(self):
        self.total_profit = self.wage + self.bonus
        return ", доход с учётом премии: {}".format(self.total_profit)


w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.wage)

p = Position()
print("\n<< Общая информация по сотруднику >>")
print(p.get_full_name() + str(p.get_full_income()) + " " + str(w._income))
'''
task4
'''


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


town = TownCar('Ока', 85, 'black', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Jeep', 200, 'yellow', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('Honda', 45, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())
'''
task5
'''


class Stationery:
    title = "\n<< Канцелярская принадлежность >>"

    def draw(self):
        print("Родительский метод класса Stationery")
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("\nРодительский метод класса Pen")
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("\nРодительский метод класса Pencil")
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("\nРодительский метод класса Handle")
        print("Запуск отрисовки маркером")


s = Stationery()
print(s.title)
s.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Handle()
h.draw()
