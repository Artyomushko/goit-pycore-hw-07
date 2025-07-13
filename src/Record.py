from typing import Optional

from src.Fields.Birthday import Birthday
from src.Fields.Name import Name
from src.Fields.Phone import Phone


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
