# coding: UTF-8
# PEP-8

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки,
# имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя,
# te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

def check(pattern, string):
    return re.search(pattern, string) is None

name_pat = '^[А-Я][а-я]*$'
email_pat = '^[a-z_\d]*@[a-z\d]*\.(com|ru|org)$'

name, last_name = input('Введите Ваши имя и фамилию через пробел: ').split()
email = input('Введите Ваш email: ')

if check(name_pat, name) and check(name_pat, last_name):
     print('Имя и фамилия введены некорректно!')
elif check(name_pat, name):
     print('Имя введенно некорректно!')
elif check(name_pat, last_name):
    print('Фамилия введена некорректно!')
else:
    print('{} {}, Ваши имя и фамилия введены корректно!'.format(name, last_name))

print('Адрес электронной почты введён некорректно!') if check(email_pat, email) else \
    print('Ваш почтовый ящик: {}'.format(email))
