# coding: UTF-8
# PEP-8

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil

file = os.path.realpath(__file__)
shutil.copyfile(file, '_copy' + file)