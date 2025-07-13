from typing import Optional

from src.AddressBook import AddressBook
from src.Record import Record


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

    record = contacts.find(name)

    if record:
        record.add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)

    return "Contact added."


@input_error
def change_contact(args: tuple[str, str, str], contacts: AddressBook) -> str:
    name, old_phone, phone = args

    record = contacts.find(name)
    if not record:
        raise KeyError(f"No such contact: {name}")

    record.edit_phone(old_phone, phone)
    return "Contact updated."


@input_error
def show_record(args: tuple[str], contacts: AddressBook) -> Optional[Record]:
    name = args[0]
    return contacts.find(name)


@input_error
def show_phones(args: tuple[str], contacts: AddressBook) -> list[str]:
    name = args[0]

    record = contacts.find(name)
    if not record:
        raise KeyError(f"No such contact: {name}")

    return list(map(lambda phone: phone.value, record.phones))


@input_error
def add_birthday(args: tuple[str, str], contacts: AddressBook) -> str:
    name, birthday = args

    record = contacts.find(name)
    if not record:
        raise KeyError(f"No such contact: {name}")

    record.add_birthday(birthday)

    return 'Birthday changed.'


@input_error
def show_birthday(args: tuple[str], contacts: AddressBook) -> list[str]:
    name = args[0]

    record = contacts.find(name)
    if not record:
        raise KeyError(f"No such contact: {name}")

    return record.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(args: tuple[str], contacts: AddressBook) -> list[dict[str, str]]:
    return list(
        map(
            lambda record: {
                'name': record.name.value,
                'birthday': record.birthday.value.strftime("%d.%m")
            },
            contacts.get_upcoming_birthdays()
        )
    )


def show_all(args: tuple[str, str], contacts: AddressBook) -> AddressBook:
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
            print(show_record(args, contacts))
        elif command == "phone":
            print(show_phones(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        elif command == "all":
            for record in show_all(args, contacts):
                print(record)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
