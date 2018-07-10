# coding: UTF-8
# PEP-8

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

list_1 = [1, 2, 4, 6, 7, 11, 25, 32, 32, 65, 121, 128, 129]

for elem in list_1:

    if list_1.index(elem) == 0:
        if (math.sqrt(elem)) % 1 == 0:
            list_2 = [math.sqrt(elem)]
    else:
        if (math.sqrt(elem)) % 1 == 0:
            list_2.append(math.sqrt(elem))

print(list_2)