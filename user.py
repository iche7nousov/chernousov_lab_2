#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_your_live(name, age):
    # Запишим введеный текст в память
    your_live = str(input("Where are you live: "))
    # Проверим - состоит ли строка только из букв
    if your_live.isalpha():
        # Выведем текст в консоль
        print(f"This is {name}\n"
              f"It is {age}\n"
              f"(S)he live in {your_live}")
        input("")
        # Если есть другие символы - вернем к вводу текста
    else:
        get_your_live(name, age)
def get_your_age(name):
    # Запишим введеный текст в память
    your_age = str(input("How old are you: ")) # Тип памяти str для проверки isdigit
    # Проверим - состоит ли строка только из цифр и возраст больше 1 и меньше 120
    if your_age.isdigit() and int(your_age) >= 1 and int(your_age) <= 120:
        # Переходим к вводу места жительства и перетаскиваем значение текста
        get_your_live(name, int(your_age))
    # Если есть другие символы - вернем к вводу текста
    else:
        get_your_age(name)
def get_your_name():
    # Запишим введеный текст в память
    your_name = str(input("What is your name: "))
    # Проверим - состоит ли строка только из букв
    if your_name.isalpha():
        # Переходим к вводу возраста и перетаскиваем значение текста
        get_your_age(your_name)
    # Если есть другие символы - вернем к вводу текста
    else:
        get_your_name()

# Если объект __name__ равен __main__ запускаем наш код
if __name__ == "__main__":
    get_your_name()
