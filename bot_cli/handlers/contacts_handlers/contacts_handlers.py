def add_contact(args, contacts): # приймає два аргументи: args, який є списком і містить ім'я та телефонний номер, та contacts, який є словником, де зберігаються контакти
    if len(args) == 0 or len(args) == 1:
        return "Arguments are required. Print 'add username 123456', where username is contact's name, and 12345 is contacts phone number."
    name, phone = args # два елементи зі списку args розпаковуються в змінні name та phone
    if name in contacts:
        return f"Contact {name} already exists"
    contacts[name] = phone # додає пару "ключ: значення" до словника контактів, використовуючи ім'я як ключ і телефонний номер як значення contacts[name] = phone.
    return f"Contact added: {name} {phone}"

def change_contact(args, contacts): # Змінити контакт 
    if len(contacts) == 0:
        return "The contacts list is empty. Print 'add username 123456' to add your first contact."
    if len(args) == 0 or len(args) == 1:
        return "Arguments are required. Print 'change username 123456', where username is contact's name, and 12345 is contacts phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"{name}'s phone changed."
    return f"The {name} is not found"

def show_phone(args, contacts): # Показати номер
    if len(contacts) == 0:
        return "The contacts list is empty. Print 'add username 123456' to add your first contact."
    if len(args) == 0:
        return "Argument is required. Print 'show username', where username is contact's name"
    name = args[0]
    if name in contacts:
        number = contacts[name]
        return f"The {name}'s phone is: {number}"
    return f"The {name} is not found"

def show_all(contacts): # показати всі контакти в списку
    if len(contacts) == 0:
        return "The contacts list is empty. Print 'add username 123456' to add your first contact."
    return f"All phone numbers: {contacts}"

def delete_contact(args, contacts): # видалити контакт
    if len(contacts) == 0:
        return "The contacts list is already empty"
    elif len(args) == 0:
        return "Argument is required. Print 'delete all', or 'delete username'."
    name = args[0]
    if name in contacts:
        del contacts[name]
        return f"The {name} has been deleted"
    elif name == "all": # видалити всі контакти
        contacts.clear()
        return "All contacts have been deleted"
    return f"The {name} is not found"
