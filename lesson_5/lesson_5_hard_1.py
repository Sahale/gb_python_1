# coding: UTF-8
# PEP-8

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print()

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def copyfile():
    if not dir_name:
        print("Необходимо указать имя исходного файла вторым параметром")
        return
    if not dir_name_add:
        print("Необходимо указать имя конечного файла третьим параметром")
        return
    try:
        shutil.copyfile(dir_name, dir_name_add)
        print('Файл успешно скопирован!')
    except:
        print('Какая-то беда!')

def removefile():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    approve = str(input('Уверен? Y/N: '))
    if approve == 'Y':
        try:
            os.remove(dir_name)
            print('Успешно удалено!')
        except FileNotFoundError:
            print('Файл не найден.')
    else:
        print('Файл НЕ удален.')

def cddir(dir_name):
    try:
        os.chdir(dir_name)
        print('Вы перешли в директорию', dir_name)
        return
    except FileNotFoundError:
        print('Директории не сущeствует!')
        return

def listcdw():
    print(os.path.join(os.getcwd(), ''))

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copyfile,
    "rm": removefile,
    "cd": cddir,
    "ls": listcdw
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    dir_name_add = sys.argv[3]
except IndexError:
    dir_name_add = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
