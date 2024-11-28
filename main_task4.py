def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "The contact exists"
        except ValueError:
            return "Please enter the correct arguments"
        except IndexError:
            return "No such contacts"

    return inner

# Парсинг введеної строки
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."



# Зміна контакту
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f'Contact {name} is not in the list'


# Показ контакту
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f'Phone number: {contacts[name]} '
    else:
        return f'Contact {name} is not in the list'


# Виведення всих номерів
def show_all(contacts):
    if not contacts:
        return "Contact list is empty"
    else:
        contact_list = "Contact list:\n"
        for name, phone in contacts.items():
            contact_list += f'Name: {name}\t phone: {phone}\n'
        return contact_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
