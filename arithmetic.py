#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def arithmetic():
    # Запишим значение ответа пользователя в память
    get_user_number = int(input("4 * 100 - 54 = напишите ответ: "))
    # Выведем значение в консоли
    print("Ответ пользователя: ", get_user_number)

    # Запишим решение компьютера в память
    get_python_number = 4 * 100 - 54
    # Выведем значение в консоли
    print("Правильный ответ: ", get_python_number)

    # Сравним значение объектов с ответами
    if get_python_number == get_user_number:
        # Если значения одинаковые
        print("Пользователь решил правильно")
    else:
        # Если значения разные
        print("Пользователь решил не правильно")

    input("")

# Если объект __name__ равен __main__ запускаем наш код
if __name__ == "__main__":
    arithmetic()