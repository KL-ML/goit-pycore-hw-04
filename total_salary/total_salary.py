# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).

import math
import re

def total_salary(path):

    # ініціалюзує змінні
    total = 0
    average = 0
    employees_quantity = 0

    try:
        # відкриває файл для читання
        with open(path, "r", encoding="utf-8") as file:

            # читає кожну строку, поки вони є
            while True:
                line = file.readline()
                if not line:
                    break

                # відсікає пошкоджені або пусті строки 
                pattern = r"\w+\,+\d+"
                match = re.search(pattern, line, re.IGNORECASE)
                if match:

                    # підраховує кількість працівників
                    employees_quantity += 1

                    # підраховує загальну заробітнку плату
                    total += int(line.split(',')[1])

                    # підраховує середню заробітну плату
                    average = math.ceil(total / employees_quantity)

        # Якщо по закінченню роботи функції кількість співробітників дорівнює нулю - повертає повідомлення
        if employees_quantity == 0:
            print("Файл пошкоджений або пустий.")

        # повертає загальну та середню заробітну платню
        return total, average

    # обробляє помилку відсутності файлу
    except FileNotFoundError:
        print("Не вдалося знайти файл.")
        return total, average
    
    # Обробляє помилку коли замість файлу вказали шлях до директорії
    except IsADirectoryError:
        print("Не вдалося знайти файл.")
        return total, average




total, average = total_salary("/Users/borysdudnyk/Documents/Pyton_goit/Pyton_conspect/python-for-magistr/hw/goit-pycore-hw-04/task-1/salary-list.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
