from typing import List

from product import Product


class Receipt:
    

    VAT_RATE = 0.075  

    def __init__(self, items: List[Product], items_count: int, discount_percent: float):
    
        self._items = items
        
        self._items_count = items_count
        
        self._discount_percent = discount_percent

    def get_sub_total(self) -> float:
    
        sub_total = 0.0
        
        for count in range(self._items_count):
        
            sub_total += self._items[count].newline_total()
            
        return sub_total

    def get_discount_amount(self) -> float:
    
        return self.get_sub_total() * (self._discount_percent / 100)

    def get_vat_amount(self) -> float:
    
        return self.get_discount_amount() * self.VAT_RATE

    def get_bill_total(self) -> float:
    
        return self.get_sub_total() - self.get_discount_amount() + self.get_vat_amount()

    def get_balance(self, amount_paid: float) -> float:
    
        return amount_paid - self.get_bill_total()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
