# Функція розбирає введений користувачем рядок на команду та її аргументи.
def parse_input(user_input): 
    cmd, *args = user_input.lower().split()
    cmd = cmd.strip()
    return cmd, *args