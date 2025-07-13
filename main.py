from collections import UserDict
from typing import Optional
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        if not value.isnumeric():
            raise ValueError("Phone number must be numeric")
        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str):
        try:
            value = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str) -> None:
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone: str) -> None:
        phone = self.find_phone(phone)
        self.phones.remove(phone)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        old_phone = self.find_phone(old_phone)
        old_phone.value = new_phone

    def find_phone(self, phone: str) -> Optional[Phone]:
        phone_field = list(filter(lambda phone_field: phone_field.value == phone, self.phones))
        if len(phone_field) == 0:
            raise ValueError("Phone not found")
        return phone_field[0]

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data[name] if name in self.data else None

    def delete(self, name: str) -> Optional[Record]:
        if name in self.data:
            record = self.data[name]
            del self.data[name]
            return record

        return None

    def get_upcoming_birthdays(self) -> list:
        birthdays = []

        today = datetime.today().date()

        for user in self.data.values():
            birthday_this_year = datetime(today.year, user.birthday.value.month, user.birthday.value.day).date()

            if birthday_this_year > today:
                next_birthday = birthday_this_year
            else:
                next_birthday = birthday_this_year.replace(year=today.year + 1)

            if (next_birthday - today).days < 7:
                birthdays.append(user)

        return birthdays


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("17.07.2002")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("0987654321")
jane_record.add_birthday("22.12.2002")

book.add_record(jane_record)

print(book.get_upcoming_birthdays()[0])
