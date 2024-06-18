from handlers import parse_input, add_contact, change_contact, show_all, show_phone, delete_contact

def main(): # управляє основним циклом обробки команд.

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) # Змінна command отримує перше значення та вважається командою, а змінна args стає списком з усіх інших значень.
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add": # "add username phone"
            print(add_contact(args, contacts))
        elif command == "change": # "change username phone" 
            print(change_contact(args, contacts))
        elif command == "phone": # "username" 
            # За цією командою бот виводить у консоль номер телефону для зазначеного контакту username
            print(show_phone(args, contacts))
        elif command == "all": # "all" 
            # За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
            print(show_all(contacts))
        elif command == "delete": # "username", "all" - видаляє всі контакти
            # За цією командою бот видаляє контакт username зі списку contacts.
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()