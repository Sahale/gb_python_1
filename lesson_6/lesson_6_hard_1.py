# coding: UTF-8
# PEP-8


# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class production:

    def buy_stock(self, material):
        print('Закупаем {}'.format(material))

    def make_skelet(self):
        print('Создаем игрушку')

    def paint(self, colour):
        print('Красим в {} цвет!'.format(colour))

    def final(self):
        print('Игрушка изготовлена!')


class fabric:

    def __init__(self, name, colour, kind, material):
        self.name = name
        self.colour = colour
        self.type = kind
        self.material = material
        # toy.production(self)
        fabric.send_to_production(self)

    def send_to_production(self):
        production.buy_stock(self, self.material)
        production.make_skelet(self)
        production.paint(self, self.colour)
        production.final(self)


a = fabric('Миша', 'Белый', 'Живтоне', 'Кожзам')
print(a.name)