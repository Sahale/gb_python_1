# coding: UTF-8
# PEP-8

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

path = os.getcwd()
print(os.listdir(path))

