from datetime import date

from items import Item


class Drug(Item):
    def __init__(self):
        self._name: str = ""
        self._price: float = 0.0
        self._expiry_date: date | None = None
        self._quantity: int = 0
        self._drug_type = ""

    @property
    def drug_type(self):
        return self._drug_type

    @drug_type.setter
    def drug_type(self, drug_type):
        self._drug_type = drug_type