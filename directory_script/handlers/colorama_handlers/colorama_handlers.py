from colorama import Fore, Style

# Оформлює вивід назви директорії
def main_dir_colored(message):
    print(f"{Fore.CYAN}DIR NAME: {message}{Fore.RESET}")

# Оформлює вивід повідомлення про помилку
def exept_colored(message):
    print(f"{Fore.RED}WARNING: {message}{Fore.RESET}")

# Оформлює вивід директорії
def file_colored(message):
    return f"{Fore.GREEN}[F]{Fore.RESET} {message}"

# Оформлює вивід файлу
def dir_colored(message):
    return f"{Fore.YELLOW}[D]{Fore.RESET} {message}"

# Оформлює відображення дерева директорії
def dir_tree_slyled(i):
    return f"{Style.DIM}{'|' * i + '-'}{Style.RESET_ALL}"

