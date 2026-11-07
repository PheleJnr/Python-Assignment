from user import User
from items import Item


class Pharmacist(User):
    def __init__(self, name: str, phone_number: str):
        self._name = name
        self._phone_number = phone_number
        self._id = None
        self._pharmacy = None

    def employed_by(self, pharmacy) -> None:
        self._pharmacy = pharmacy

    @property
    def name(self):
        return self._name

    @property
    def phone_number(self):
        return self._phone_number

    @name.setter
    def name(self, name):
        self._name = name

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, given_id):
        self._id = given_id

    def search_product(self, product_name: str) -> Item :
        return self._pharmacy.search_item(product_name)

    def check_product_available(self, product_name: str, given_quantity: float) -> bool :
        found_item = self.search_product(product_name)
        if found_item is None:
            raise ValueError(f"Product {product_name} not found in pharmacist")
        return found_item.quantity >= given_quantity and not found_item.is_expired()

    def view_inventory(self) -> list:
        return self._pharmacy.get_inventory()