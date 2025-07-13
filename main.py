from src.AddressBook import AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "No such contact."

    return inner


@input_error
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: tuple[str, str], contacts: AddressBook) -> str:
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added."


@input_error
def change_contact(args: tuple[str, str], contacts: AddressBook) -> str:
    name, phone = args

    if name not in contacts:
        raise KeyError(f"No such contact: {name}")

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: tuple[str], contacts: dict) -> str:
    name = args[0]
    return contacts[name]


def show_all(args: tuple[str, str], contacts: dict) -> dict:
    return contacts


def main() -> None:
    contacts = AddressBook()
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
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
