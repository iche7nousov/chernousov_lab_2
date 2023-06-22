#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Запросите у пользователя четыре числа (файл numbers.py). Отдельно сложите первые два и
отдельно вторые два. Разделите первую сумму на вторую. Выведите результат на экран так,
чтобы ответ содержал две цифры после запятой.
"""
def numbers():
    # Запишим значение в память
    one = float(input("1: "))
    two = float(input("2: "))
    three = float(input("3: "))
    four = float(input("4: "))

    first_sum = one + two
    last_sum = three + four
    answer = first_sum / last_sum
    print("%.2f" % answer)

# Если объект __name__ равен __main__ запускаем наш код
if __name__ == "__main__":
    numbers()
