# coding: UTF-8
# PEP-8

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = [1, 2, 3, 5, 5, 7, 9, 11, 'test', 'test2', 'test4', 'test2']
list_2 = [4, 5, 6, 7, 8, 9, 10, 'test2']

for elem in list_2:
    while list_1.count(elem) != 0:
        list_1.remove(elem)
print(list_1)