from datetime import datetime

from src.Fields.Field import Field


class Birthday(Field):
    def __init__(self, value: str):
        try:
            value = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")