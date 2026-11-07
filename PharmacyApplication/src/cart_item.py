class CartItem :
    def __init__(self , item_id : int, quantity : int , sub_total : float ,):
        self.item_id : int = item_id
        self.quantity : float = quantity
        self.sub_total : float = sub_total


    def calculate_subtotal(self) -> float :
        self.sub_total = (self.quantity * self.sub_total)
        return self.sub_total

    def update_quantity (self, restocked_quantity : float):
        self.quantity += restocked_quantity