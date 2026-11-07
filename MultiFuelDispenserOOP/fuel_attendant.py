from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_DOWN, ROUND_HALF_UP

from fuel import Fuel


class FuelAttendant:

    MIN_LITERS = Decimal("1")
    MAX_LITERS = Decimal("50")
    CENT = Decimal("0.01")

    def __init__(self, full_name, dispenser):
        if not isinstance(full_name, str) or not full_name.strip():
            raise ValueError("Attendant name cannot be empty.")

        self.full_name = full_name.strip().title()
        self.dispenser = dispenser
        self.transactions = []


    @staticmethod
    def _to_money_decimal(value, label):
        if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
            raise ValueError(f"{label} must be a number.")

        number = Decimal(str(value))

        if not number.is_finite():
            raise ValueError(f"{label} must be a finite number.")

        if number <= 0:
            raise ValueError(f"{label} must be greater than zero.")

        try:
            rounded = number.quantize(FuelAttendant.CENT)
        except InvalidOperation:
            raise ValueError(f"{label} is too large.")

        if number != rounded:
            raise ValueError(f"{label} can have at most 2 decimal places.")

        return rounded

    def _record_transaction(self, fuel, liters, total_amount):
        transaction = {
            "transaction_id": len(self.transactions) + 1,
            "attendant": self.full_name,
            "fuel_name": fuel.fuel_name,
            "price_per_liter": Decimal(str(fuel.price_per_liter)),
            "liters": liters,
            "total_amount": total_amount,
            "timestamp": datetime.now(),
        }
        self.transactions.append(transaction)
        return transaction


    def add_fuel(self, fuel_name, price_per_liter, quantity):
        self.dispenser.add_fuel(Fuel(fuel_name, price_per_liter, quantity))

    def get_available_fuels(self):
        return self.dispenser.list_fuels()

    def update_fuel_price(self, fuel_name, new_price):
        self.dispenser.update_fuel_price(fuel_name, new_price)

    def restock_fuel(self, fuel_name, liters):
        self.dispenser.restock_fuel(fuel_name, liters)


    def dispense_by_liters(self, fuel_name, liters):
        liters = self._to_money_decimal(liters, "Liters")

        if not self.MIN_LITERS <= liters <= self.MAX_LITERS:
            raise ValueError(
                f"Liters must be between {self.MIN_LITERS} and {self.MAX_LITERS}."
            )

        fuel = self.dispenser.get_fuel(fuel_name)
        price = Decimal(str(fuel.price_per_liter))
        total_amount = (liters * price).quantize(self.CENT, ROUND_HALF_UP)

        self.dispenser.dispense_fuel(fuel_name, float(liters))

        return self._record_transaction(fuel, liters, total_amount)

    def dispense_by_amount(self, fuel_name, amount):
        amount = self._to_money_decimal(amount, "Amount")

        fuel = self.dispenser.get_fuel(fuel_name)
        price = Decimal(str(fuel.price_per_liter))

        if amount < price:
            raise ValueError(
                f"Amount must be at least the price of one liter "
                f"(₦{price:,.2f})."
            )

        liters = (amount / price).quantize(self.CENT, ROUND_DOWN)

        self.dispenser.dispense_fuel(fuel_name, float(liters))

        return self._record_transaction(fuel, liters, amount)


    def get_transactions(self):
        return list(self.transactions)

    def get_transaction(self, transaction_id):
        if isinstance(transaction_id, bool) or not isinstance(transaction_id, int):
            raise ValueError("Transaction ID must be a whole number.")

        if not 1 <= transaction_id <= len(self.transactions):
            raise ValueError("Transaction not found.")

        return self.transactions[transaction_id - 1]

    def format_transaction_history(self):
        if not self.transactions:
            return "No transactions yet."

        lines = ["ID  Fuel         Litres    Total (₦)"]
        for t in self.transactions:
            lines.append(
                f"{t['transaction_id']:<3} {t['fuel_name']:<12} "
                f"{t['liters']:>6}    {t['total_amount']:>12,.2f}"
            )
        return "\n".join(lines)

    def generate_receipt(self, transaction_id):
        t = self.get_transaction(transaction_id)
        line = "=" * 34
        return "\n".join([
            line,
            "      MULTI-FUEL DISPENSER RECEIPT",
            line,
            f"Receipt No : {t['transaction_id']}",
            f"Date       : {t['timestamp']:%Y-%m-%d %H:%M:%S}",
            f"Attendant  : {t['attendant']}",
            f"Fuel       : {t['fuel_name']}",
            f"Price/Litre: ₦{t['price_per_liter']:,.2f}",
            f"Litres     : {t['liters']}",
            f"Total Paid : ₦{t['total_amount']:,.2f}",
            line,
            "        Thank you. Drive safely!",
            line,
        ])

    def print_receipt(self, transaction_id):
        print(self.generate_receipt(transaction_id))