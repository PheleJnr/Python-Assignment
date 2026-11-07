from datetime import date

from cart_item import CartItem


class Purchase:
    def __init__(self):
        self._transaction_id = None
        self._date : date | None = None
        self._total_amount : float= None
        self._purchased_items : list[CartItem] = None

    def get_total_amount(self) -> float:
        return self._total_amount

    def get_purchased_items(self) -> list[CartItem]:
        return self._purchased_items

    @property
    def transaction_id(self) -> int:
        return self._transaction_id
    @transaction_id.setter
    def transaction_id(self, transaction_id: int):
        self._transaction_id = transaction_id

    @property
    def date(self) -> date:
        return self._date
    @date.setter
    def date(self, date: date):
        self._date = date