# coding: utf-8
# PEP-8

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Пожалуйста, введите Ваш возраст: "))
if age < 18:
    print("Доступ закрыт!")
else:
    print("Доступ разрешён.")
