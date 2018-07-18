# coding: UTF-8
# PEP-8

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

while True:
    i = 0
    value = int(input("Пожалуйста, введите необходимую длину списка: "))
    while i < value:
        if i == 0:
            list_1 = [random.randint(-100, 100)]
            i += 1
        else:
            list_1.append(random.randint(-100, 100))
            i += 1
    print(list_1)