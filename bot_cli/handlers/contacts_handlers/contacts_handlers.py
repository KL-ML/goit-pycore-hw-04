# Функція додає нові контакти до списку
def add_contact(args, contacts): 
    # перевірка на відсутність двох аргументів в запиті
    if len(args) == 0 or len(args) == 1:
        return "Arguments are required. Print 'add username 123456', where username is contact's name, and 12345 is contacts phone number."
    name, phone = args
    # перевірка чи контакт вже існує в списку
    if name in contacts:
        return f"Contact {name} already exists"
    # додає новий контакт в список
    contacts[name] = phone
    # повертає повідомлення, що контакт доданий в список
    return f"Contact added: {name} {phone}"

# Функція змінює номер телефону існуючого контакту
def change_contact(args, contacts):
    # перевіряє чи список контактів пустий
    if len(contacts) == 0:
        return "The contacts list is empty. Print 'add username 123456' to add your first contact."
    # перевірка на відсутність двох аргументів в запиті
    if len(args) == 0 or len(args) == 1:
        return "Arguments are required. Print 'change username 123456', where username is contact's name, and 12345 is contacts phone number."
    name, phone = args
    # якщо контакт є в списку - редагує
    if name in contacts:
        contacts[name] = phone
        return f"{name}'s phone changed."
    # якщо контакту немає в списку - повертає повідомлення
    return f"The {name} is not found"

# Функція виводить в консоль номер телефону існуючого контакту
def show_phone(args, contacts):
    # перевіряє чи список контактів пустий
    if len(contacts) == 0:
        return "The contacts list is empty. Print 'add username 123456' to add your first contact."
    # перевірка на відсутність одного аргументу в запиті
    if len(args) == 0:
        return "Argument is required. Print 'show username', where username is contact's name"
    name = args[0]
    # якщо контакт є в списку - виводить дані в консоль
    if name in contacts:
        number = contacts[name]
        return f"The {name}'s phone is: {number}"
    # якщо контакту немає в списку - повертає повідомлення
    return f"The {name} is not found"

# Функція показує всі контакти в списку
def show_all(contacts): 
    # перевіряє чи список контактів пустий
    if len(contacts) == 0:
        return "The contacts list is empty. Print 'add username 123456' to add your first contact."
    # якщо список не пустий - виводить всі дані зі списку в консоль
    return f"All phone numbers: {contacts}"

# Функція видаляє контакти
def delete_contact(args, contacts): # видалити контакт
    # перевіряє чи список контактів пустий
    if len(contacts) == 0:
        return "The contacts list is already empty"
    # перевірка на відсутність одного аргументу в запиті
    elif len(args) == 0:
        return "Argument is required. Print 'delete all', or 'delete username'."
    name = args[0]
    # якщо контакт є в списку - видаляє його зі списку
    if name in contacts:
        del contacts[name]
        return f"The {name} has been deleted"
    # якщо переданий агрумент "all" - видаляє всі контакти
    elif name == "all":
        contacts.clear()
        return "All contacts have been deleted"
    # якщо контакту немає в списку - повертає повідомлення
    return f"The {name} is not found"
