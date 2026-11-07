from dispenser import Dispenser
from fuel_attendant import FuelAttendant

MENU = """
========== MULTI-FUEL DISPENSER SYSTEM ==========
1. Add a fuel product
2. View available fuels and stock
3. Update a fuel price
4. Restock fuel
5. Dispense fuel by litres
6. Dispense fuel by Naira amount
7. View transaction history
8. Print a receipt
9. Exit
=================================================
"""


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Error: This cannot be empty.")


def parse_number(text):
    cleaned = text.strip().replace(",", "").replace("₦", "")
    try:
        number = float(cleaned)
    except ValueError:
        raise ValueError(f"'{text}' is not a valid number.")

    if number != number or number in (float("inf"), float("-inf")):
        raise ValueError(f"'{text}' is not a valid number.")

    return int(number) if number.is_integer() else number


def read_number(prompt):
    while True:
        try:
            return parse_number(input(prompt))
        except ValueError as error:
            print(f"Error: {error}")


def read_menu_choice(prompt="Choose an option (1-9): "):
    while True:
        text = input(prompt).strip()
        if text.isdigit() and 1 <= int(text) <= 9:
            return int(text)
        print("Error: Please enter a number from 1 to 9.")


def format_fuels(fuels):
    if not fuels:
        return "No fuels available yet."

    lines = [f"{'Fuel':<12} {'Price/Litre':>14} {'Stock (L)':>12}"]
    for fuel in fuels:
        lines.append(
            f"{fuel.fuel_name:<12} ₦{fuel.price_per_liter:>12,.2f} "
            f"{fuel.quantity:>12,.2f}"
        )
    return "\n".join(lines)


def add_fuel_option(attendant):
    name = read_text("Fuel name: ")
    price = read_number("Price per litre (₦): ")
    quantity = read_number("Starting stock (litres): ")
    attendant.add_fuel(name, price, quantity)
    print(f"{name.title()} added successfully.")


def view_fuels_option(attendant):
    print(format_fuels(attendant.get_available_fuels()))


def update_price_option(attendant):
    print(format_fuels(attendant.get_available_fuels()))
    name = read_text("Fuel name: ")
    price = read_number("New price per litre (₦): ")
    attendant.update_fuel_price(name, price)
    print("Price updated successfully.")


def restock_option(attendant):
    print(format_fuels(attendant.get_available_fuels()))
    name = read_text("Fuel name: ")
    liters = read_number("Litres to add: ")
    attendant.restock_fuel(name, liters)
    print("Fuel restocked successfully.")


def dispense_by_liters_option(attendant):
    print(format_fuels(attendant.get_available_fuels()))
    name = read_text("Fuel name: ")
    liters = read_number("Litres to buy (1 - 50): ")
    transaction = attendant.dispense_by_liters(name, liters)
    print(attendant.generate_receipt(transaction["transaction_id"]))


def dispense_by_amount_option(attendant):
    print(format_fuels(attendant.get_available_fuels()))
    name = read_text("Fuel name: ")
    amount = read_number("Amount to spend (₦): ")
    transaction = attendant.dispense_by_amount(name, amount)
    print(attendant.generate_receipt(transaction["transaction_id"]))


def view_history_option(attendant):
    print(attendant.format_transaction_history())


def print_receipt_option(attendant):
    transactions = attendant.get_transactions()
    if not transactions:
        print("No transactions yet, so there is no receipt to print.")
        return

    text = input(
        "Receipt number (press Enter for the latest): "
    ).strip()
    if text == "":
        transaction_id = transactions[-1]["transaction_id"]
    elif text.isdigit():
        transaction_id = int(text)
    else:
        raise ValueError("Receipt number must be a whole number.")

    attendant.print_receipt(transaction_id)


ACTIONS = {
    1: add_fuel_option,
    2: view_fuels_option,
    3: update_price_option,
    4: restock_option,
    5: dispense_by_liters_option,
    6: dispense_by_amount_option,
    7: view_history_option,
    8: print_receipt_option,
}


def run_menu(attendant):

    while True:
        print(MENU)
        choice = read_menu_choice()

        if choice == 9:
            print("Goodbye!")
            return

        try:
            ACTIONS[choice](attendant)
        except ValueError as error:
            print(f"Error: {error}")


def main():
    print("Welcome to PHELEJNR MULTI-FUEL DISPENSER SYSTEM!")

    while True:
        try:
            attendant = FuelAttendant(read_text("Attendant full name: "), Dispenser())
            break
        except ValueError as error:
            print(f"Error: {error}")

    print(f"Hello, {attendant.full_name}!")
    run_menu(attendant)


if __name__ == "__main__":
    main()