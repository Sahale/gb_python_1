# coding: UTF-8
# PEP-8

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

from collections import Counter

list_1 = [1, 2, 4, 5, 6, 2, 5, 2]

# а)
list_2 = list(set(list_1))
# б)
# Генератор. Пробегается по всем элементам списка, возвращая значение и число повторений. Если число
# повторений (val) равно единичке, то вносим элемент в список.
list_3 = [i for i, val in Counter(list_1).items() if val == 1 ]
print(list_3)
