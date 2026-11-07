from fuel import Fuel

class Dispenser:

    def __init__(self):
        self.fuels = {}

    def add_fuel(self, fuel):
        if not isinstance(fuel, Fuel):
            raise ValueError("Only Fuel objects can be added.")

        fuel_name_key = fuel.fuel_name.lower()

        if fuel_name_key in self.fuels:
            raise ValueError("This fuel already exists.")

        self.fuels[fuel_name_key] = fuel

    def get_fuel(self, fuel_name):
        if not isinstance(fuel_name, str) or not fuel_name.strip():
            raise ValueError("Fuel name cannot be empty.")

        fuel_name_key = fuel_name.strip().lower()

        if fuel_name_key not in self.fuels:
            raise ValueError("Fuel not found.")

        return self.fuels[fuel_name_key]

    def list_fuels(self):
        return list(self.fuels.values())

    def update_fuel_price(self, fuel_name, new_price):
        fuel = self.get_fuel(fuel_name)
        fuel.update_price(new_price)

    def restock_fuel(self, fuel_name, liters):
        fuel = self.get_fuel(fuel_name)
        fuel.restock_fuel(liters)

    def dispense_fuel(self, fuel_name, liters):
        fuel = self.get_fuel(fuel_name)
        fuel.dispense_fuel(liters)