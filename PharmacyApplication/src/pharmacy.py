from admin import Admin
from pharmacist import Pharmacist
from items import Item


class Pharmacy:
    def __init__(self, name: str, employed_admin: Admin):
        self.name = name
        self.address = "Lagos"
        self.admin = employed_admin
        self.inventory: list[Item] = []
        self.pharmacists: list[Pharmacist] = []

    def add_item(self, item: Item, quantity: int) -> None:
        self._validate_item(item)
        item.quantity = quantity
        self.inventory.append(item)

    def _validate_item(self, given_item: Item) -> None:
        found_item = self._find_item(given_item.name)
        if found_item is not None:
            raise ValueError("Pharmacy already has this item")

    def restock_item(self, item_name, restock_quantity: int) -> None:
        found_item = self._find_item(item_name)
        if found_item is None:
            raise ValueError("Pharmacy doesn't have this item")
        found_item.quantity += restock_quantity

    def _find_item(self, given_item_name: str) -> Item:
        for item in self.inventory:
            if item.name.lower() == given_item_name.lower():
                return item
        return None

    def search_item(self, item_name: str) -> Item:
        search_item = self._find_item(item_name)
        return search_item

    def get_inventory(self):
        return self.inventory

    def register_pharmacist(self, pharmacist: Pharmacist) -> None:
        self._validate_id(pharmacist.id)
        self.pharmacists.append(pharmacist)

    def get_pharmacist(self, pharmacist_id: int) -> Pharmacist:
        found_pharmacist = self._find_pharmacist(pharmacist_id)
        return found_pharmacist

    def check_expiry(self):
        return [item for item in self.inventory if item.is_expired()]

    def _validate_id(self, given_id: int) -> None:
        if given_id < 0:
            raise ValueError("Pharmacy id cannot be negative")
        found_pharmacist = self._find_pharmacist(given_id)
        if found_pharmacist is not None:
            raise ValueError("Pharmacy already has this pharmacist")

    def _find_pharmacist(self, given_id: int) -> Pharmacist:
        for each_pharmacist in self.pharmacists:
            if each_pharmacist.id == given_id:
                return each_pharmacist
        return None