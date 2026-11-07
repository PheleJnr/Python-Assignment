from datetime import date


class Item:
    def __init__(self):
        self._name: str = ""
        self._price: float = 0.0
        self._expiry_date: date | None = None
        self._quantity: int = 0


    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def expiry_date(self):
        return self._expiry_date

    @property
    def quantity(self):
        return self._quantity

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @expiry_date.setter
    def expiry_date(self, expiry_date : date):
        self._expiry_date = expiry_date

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    def is_expired(self) -> bool:
        return self._expiry_date is not None and self._expiry_date < date.today()