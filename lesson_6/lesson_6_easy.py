# coding: UTF-8
# PEP-8

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class car:

    def __init__(self, speed = 60, color = 'white', name = 'LADA', is_police = 'No'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go, go, go!')

    def stop(self):
        print('Stop!')

    def turn(self, direction):
        print('Make {} turn!'.format(direction))

class TownCar(car):
    def __init__(self, speed=60, color='blue', name='KIA', is_police='No'):
        super().__init__(speed, color, name, is_police)

a = TownCar()
print(a.color)
