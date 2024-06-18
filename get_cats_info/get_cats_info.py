# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).

import re

def get_cats_info(path):

    # інізіалізує список
    cats_info = []

    try:
        # відкриває файл для читання
        with open(path, "r", encoding="utf-8") as file:

            # читає кожну строку поки вони є
            while True:
                line = file.readline()
                if not line:
                    break

                # відсікає пошкоджені або пусті строки
                pattern = r"\w+\,+\w+\,+\d"
                match = re.search(pattern, line, re.IGNORECASE)
                if match:

                    # перетворює строку у словник і додає до списку
                    l = line.strip().split(',')
                    one_cat_info = {'id' : l[0], 'name' : l[1], 'age' : l[2].removesuffix('\n')}
                    cats_info.append(one_cat_info)

        # Якщо по закінченню роботи функції список пустий - повертає повідомлення
        if cats_info == []:
            print("Файл пошкоджений або пустий.")

        # Повертає список словників з інформацією про котів
        return cats_info

    # Обробляє помилку відсутності файлу за вказаним шляхом, або вказаний шлях пошкоджений
    except FileNotFoundError:
        print("Не вдалося знайти файл.")
        return cats_info
    
    # Обробляє помилку коли замість файлу вказаний шлях до директорії
    except IsADirectoryError:
        print("Не вдалося знайти файл.")
        return cats_info
    



cats_info = get_cats_info("/Users/borysdudnyk/Documents/Pyton_goit/Pyton_conspect/python-for-magistr/hw/goit-pycore-hw-04/task-2/cats_info.txt")
print(cats_info)