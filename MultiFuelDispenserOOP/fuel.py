import math

class Fuel:

    def __init__(self, fuel_name, price_per_liter, quantity):
        if not isinstance(fuel_name, str) or not fuel_name.strip():
            raise ValueError("Fuel name cannot be empty.")

        self.fuel_name = fuel_name.strip().title()
        self.price_per_liter = self._validate_price(price_per_liter)
        self.quantity = self._validate_quantity(quantity)

    @staticmethod
    def _validate_number(value, label):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{label} must be a number.")

        if not math.isfinite(value):
            raise ValueError(f"{label} must be a finite number.")

        return value

    @staticmethod
    def _validate_price(price):
        price = Fuel._validate_number(price, "Price")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        return float(price)

    @staticmethod
    def _validate_quantity(quantity):
        quantity = Fuel._validate_number(quantity, "Quantity")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        return float(quantity)

    def update_price(self, new_price):
        self.price_per_liter = self._validate_price(new_price)

    def restock_fuel(self, liters):
        liters = self._validate_quantity(liters)

        if liters == 0:
            raise ValueError("Restock quantity must be greater than zero.")

        self.quantity += liters

    def dispense_fuel(self, liters):
        liters = self._validate_quantity(liters)

        if liters == 0:
            raise ValueError("Dispensed quantity must be greater than zero.")

        if liters > self.quantity:
            raise ValueError("Insufficient fuel in stock.")

        self.quantity -= liters