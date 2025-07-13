from src.Fields.Field import Field


class Phone(Field):
    def __init__(self, value: str):
        if not value.isnumeric():
            raise ValueError("Phone number must be numeric")
        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)
