from collections import UserDict
from datetime import datetime
from typing import Optional


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
