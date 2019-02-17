# coding: UTF-8
# PEP-8

# """
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
# """


import random
import sys


class Checker:

    def checkinstance(digit, card):
        checkstate = 0
        for lines in card:
            if digit in lines.values():
                checkstate = 1
        return checkstate


class DrillerKiller:

    def strikeexisitingvalue(digit, card):
        for lines in card:
            if digit in lines.values():
                index = [key for key, value in lines.items() if value == digit]
                index = int(index[0])
                lines[index] = ''
                return card
        pass


class LottoCard:

    def __init__(self):
        self.first_line = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        self.second_line = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        self.third_line = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        self.card = []
        LottoCard.fullfill_card(self)

    def fullfill_card(self):
        self.generator(self.first_line)
        self.card.append(self.first_line)
        self.generator(self.second_line)
        self.card.append(self.second_line)
        self.generator(self.third_line)
        self.card.append(self.third_line)

    def generator(self, current_line):
        self.numinlines = 1
        self.random_indexes = []
        while self.numinlines <= 5:
            self.randomindex = random.randint(1, 9)
            if self.randomindex in self.random_indexes:
                pass
            else:
                self.random_indexes.append(self.randomindex)
                self.numinlines += 1
        self.random_indexes.sort()
        self.valuesinlines = []
        self.numofvalues = 1
        while self.numofvalues <= 5:
            self.randomvalue = random.randint(1, 90)
            if self.randomvalue in self.valuesinlines or Checker.checkinstance(self.randomvalue, self.card) == 1:
                pass
            else:
                self.valuesinlines.append(self.randomvalue)
                self.numofvalues += 1
        self.valuesinlines.sort()
        self.linespos = 0
        while self.linespos <= 4:
            current_line[self.random_indexes[self.linespos]] = self.valuesinlines[self.linespos]
            self.linespos += 1
        return current_line


class BeautifulOutput:

    def card_output(player_card, name):
        if name == "Player":
            print('****** Ваша карточка ******')
        else:
            print('*** Карточка компьютера ***')
        for diction in player_card:
            for value in diction:
                if diction[value] == '':
                    sys.stdout.write('  |')
                else:
                    if diction[value] < 10:
                        sys.stdout.write(' ' + str(diction[value]) + '|')
                    else:
                        sys.stdout.write(str(diction[value]) + '|')
            print()
        print('***************************')


class Game:

    def start():
        Player = LottoCard()
        Enemy = LottoCard()
        valuesforgame = []
        iter = 1
        BeautifulOutput.card_output(Player.card, 'Player')
        BeautifulOutput.card_output(Enemy.card, 'Enemy')
        while iter <= 90:
            value = random.randint(1, 90)
            if value in valuesforgame:
                pass
            else:
                valuesforgame.append(value)
                iter += 1
                print('Выпал бочонок ', value)
                answer = input("Вы хотите вычеркнуть значение? Y/Any other key: ")
                if Checker.checkinstance(value, Player.card) == 1 and answer == 'Y':
                    DrillerKiller.strikeexisitingvalue(value, Player.card)
                    BeautifulOutput.card_output(Player.card, 'Player')
                elif Checker.checkinstance(value, Player.card) == 0 and answer != 'Y':
                    BeautifulOutput.card_output(Player.card, 'Player')
                    pass
                else:
                    print('Вы проиграли!')
                    break
                if Checker.checkinstance(value, Enemy.card) == 1:
                    DrillerKiller.strikeexisitingvalue(value, Enemy.card)
                BeautifulOutput.card_output(Enemy.card, 'Enemy')

Game.start()
