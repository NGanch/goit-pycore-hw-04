def parse_input(user_input):
    """Розбір введеної користувачем команди."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    """Додавання нового контакту."""
    if len(args) < 2:
        return "Error: Provide both a name and a phone number."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"Contact {name} added."


def change_contact(args, contacts):
    """Зміна існуючого контакту."""
    if len(args) < 2:
        return "Error: Provide both a name and a new phone number."
    name, new_phone = args[0], args[1]
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        return f"Error: Contact {name} not found."


def show_phone(args, contacts):
    """Пошук номера телефону за ім'ям."""
    if len(args) < 1:
        return "Error: Provide a name to search for."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."


def show_all(contacts):
    """Вивід усіх контактів."""
    if not contacts:
        return "No contacts found."
    result = ["Contacts:"]
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    """Основна функція взаємодії з користувачем."""
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()