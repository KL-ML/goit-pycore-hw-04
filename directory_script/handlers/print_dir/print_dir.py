from handlers import dir_tree_slyled, dir_colored, file_colored

# Функція приймає шлях до головної директорії, структуру якої потрібно відобразити
# Функція переберає вміст директорії і кожної вкладеної директорії аж до максимальної глибини вкладеності
def print_dir(directory, i = 0):

    # Змінна і підраховує рівні вкладеності директорій
    i += 1

    # Перебирає вміст директорії
    for path in directory.iterdir():
        relative_path = path.relative_to(directory)

        # Якщо файл - друкує його назву і оформлення відповідно ітерації
        if path.is_file():
            print(dir_tree_slyled(i) + file_colored(relative_path))
        # Якщо директорія - друкує її назву і оформлення відповідно ітерації
        elif path.is_dir():
            print(dir_tree_slyled(i) + dir_colored(relative_path))
            # Перебирає вміст цієї директорії
            print_dir(path, i)
