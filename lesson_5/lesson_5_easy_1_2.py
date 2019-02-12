# coding: UTF-8
# PEP-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dir = (os.getcwd() + '/')

i = 1

while i <= 9:
    try:
        os.rmdir(dir + 'dir_' + str(i))
    except FileNotFoundError:
        pass
    i += 1

