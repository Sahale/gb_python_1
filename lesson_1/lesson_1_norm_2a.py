# coding: utf-8
# PEP-8

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;


# Здесь представлен вариант, обрабатывающий и строки!


a = (input("Введите первую переменную: "))
b = (input("Введите вторую переменную: "))

a = a + b
b = a[:-len(b)]
a = a[len(b):]

print("Первая переменная:", a)
print("Вторая переменная:", b)
