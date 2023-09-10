def input_error(func): # Обробка вийнятків
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs), None
        except (KeyError, ValueError, IndexError) as exc:
            return None, exc
    return inner

contacts = {}  # Словник для зберігання контактів.

@input_error
def add(name, phone): # Створюємо новий контакт
    contacts[name] = phone
    return f"Added {name} with phone number {phone}."

@input_error
def change(name, phone): # Зміна номеру створеного контакта
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone number for {name} to {phone}."

@input_error
def phone(name): # Показуємо номер телефона конкретного імені
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(): #Всі контакти
    if contacts:
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def parse_command(user_input): #Розбіваемо на команду та параметр
    parts = user_input.split()
    command = parts[0]

    if command in ["add", "change"]:
        if len(parts) < 3:
            raise ValueError
        return command, parts[1], " ".join(parts[2:])
    elif command == "phone":
        if len(parts) < 2:
            raise IndexError
        return command, parts[1]
    elif ' '.join(parts) == "show all":
        return "show all",
    else:
        return command,

def main(): #Основна функція
    while True:
        user_input = input("\nEnter command: ").strip().lower()

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        parsed_input, exc = parse_command(user_input)

        if exc:
            if isinstance(exc, ValueError):
                print("Give me name and phone please!")
                continue
            elif isinstance(exc, IndexError):
                print("Enter user name!")
                continue
            elif isinstance(exc, KeyError):
                print("This name is not found in the contact list!")
                continue

        command = parsed_input[0]

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            _, name, phone_number = parsed_input
            result, _ = add(name, phone_number)
            print(result)
        elif command == "change":
            _, name, phone_number = parsed_input
            result, _ = change(name, phone_number)
            print(result)
        elif command == "phone":
            _, name = parsed_input
            result, _ = phone(name)
            print(result)
        elif command == "show all":
            result, _ = show_all()
            print(result)
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
