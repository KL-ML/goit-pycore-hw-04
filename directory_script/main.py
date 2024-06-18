from pathlib import Path
import sys
from handlers import print_dir
from handlers import main_dir_colored, exept_colored

def main():
    try:
        # Приймає аргумент від користувача 
        directory = Path(sys.argv[1])

        # Виводить оформлену назву основної директорії
        main_dir_colored(directory.name)

        # Виводить оформлену структуру директорії
        print_dir(directory)

    # Обробляє помилку неправильного або пошкодженого шляху
    except FileNotFoundError:
        exept_colored('No such file or directory or path is wrong')
    
    # Обробляє помилку, коли шлях вказує на файл, а не на директорію
    except NotADirectoryError:
        exept_colored('Not a directory')

if __name__ == '__main__':
    main()