from handlers import parse_input, add_contact, change_contact, show_all, show_phone, delete_contact

def main(): # управляє основним циклом обробки команд.

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) # Змінна command отримує перше значення та вважається командою, а змінна args стає списком з усіх інших значень.
        
        # завершується при введенні команди "close" або "exit"
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # вітається при введенні команди "hello"
        elif command == "hello":
            print("How can I help you?")
        # додає новий контакт при введенні команди "add [ім'я] [номер телефону]"
        elif command == "add":
            print(add_contact(args, contacts))
        # змінює номер телефону контакту при введенні команди "change [ім'я] [новий номер телефону]" 
        elif command == "change": 
            print(change_contact(args, contacts))
        # За командою "phone [ім'я]" бот виводить у консоль номер телефону для зазначеного контакту
        elif command == "phone":
            print(show_phone(args, contacts))
        # За командою "all" бот виводить всі збереженні контакти з номерами телефонів у консоль.
        elif command == "all":
            print(show_all(contacts))
        # За командою "delete all" бот видаляє всі контакти.
        # За командою "delete [ім'я]" бот видаляє зазначений контакт.
        elif command == "delete": 
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()