class Product:
    

    def __init__(self, name: str, quantity: int, unit_price: float):
    
        self._name = name
        
        self._quantity = quantity
        
        self._unit_price = unit_price

    def get_name(self) -> str:
    
        return self._name

    def get_quantity(self) -> int:
    
        return self._quantity

    def get_unit_price(self) -> float:
    
        return self._unit_price

    def newline_total(self) -> float:
        
        return self._quantity * self._unit_price
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
