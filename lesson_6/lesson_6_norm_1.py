# coding: UTF-8
# PEP-8

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random


class Person:

    def __init__(self, health = 50, damage = 5, armor = 3):
        self.health = health
        self.damage = damage
        self.armor = armor

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_armor(self):
        return self.armor

    def set_health(self, points):
        self.health -= points


class Player(Person):

    def __init__(self, health = random.randint(40,60), damage = random.randint(1,10), armor = random.randint(1,10)):
        super().__init__(health, damage, armor)

class Enemy(Person):

    def __init__(self, health=random.randint(40, 60), damage = random.randint(1,10), armor=random.randint(1, 10)):
        super().__init__(health, damage, armor)


class battle:


    def attack(last_attack):
        while player.get_health() > 0 and enemy.get_health() > 0:
            if last_attack == 'player':
                battle.damage('Enemy', 'Player')
                last_attack = 'enemy'
                if player.get_health() <= 0:
                    print("Ты проиграл!")
                    exit()
            else:
                battle.damage('Player', 'Enemy')
                last_attack = 'player'
                if enemy.get_health() <= 0:
                    print("Ты выиграл!")
                    exit()



    def damage(attacker, defender):
        if attacker == 'Player':
            rand = random.randint(1,9)
            print('Буст игрока:', rand)
            if (player.get_damage() + rand) > enemy.get_armor():
                hit = (player.get_damage() + rand) - enemy.get_armor()
                enemy.set_health(hit)
                print('Вы нанесли {} урона!'.format(hit))
                print('У врага осталось {} HP!'.format(enemy.get_health()))
            else:
                print('Броня не пробита!')
        if attacker == 'Enemy':
            rand = random.randint(1, 9)
            print('Буст врага:', rand)
            if (enemy.get_damage() + rand) > player.get_armor():
                hit = (enemy.get_damage() + rand) - player.get_armor()
                player.set_health(hit)
                print('Вам нанесли {} урона!'.format(hit))
                print('У Вас осталось {} HP!'.format(player.get_health()))
            else:
                print('Вас не пробили!')



attacker = ['player', 'enemy']
player = Player()
enemy = Enemy()
last_attack = random.choice(attacker)

print('Игрок:', player.get_health(), player.get_armor(), player.get_damage())
print('Враг:', enemy.get_health(), enemy.get_armor(), enemy.get_damage())

battle.attack(last_attack)