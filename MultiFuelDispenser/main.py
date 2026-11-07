from multi_fuel_dispenser import (
    FUELS,
    MAX_LITERS,
    MIN_LITERS,
    calculate_amount,
    calculate_liters,
    is_valid_amount,
    is_valid_liters,
    make_history,
    make_receipt,
    record_transaction,
    text_to_number,
)


def buy_petroleum(transactions):
    print("Available petroleum")
    for number, (name, price) in FUELS.items():
        print(f"    {number}. {name:<10} => {price} /Liter")

    choice = input("Enter your input: ").strip()
    while not (choice.isascii() and choice.isdigit() and int(choice) in FUELS):
        print(f"Choose a number between 1 and {len(FUELS)} !!!")
        choice = input("Enter operation: ").strip()
    name, price = FUELS[int(choice)]

    mode = input("Liter or Amount: ").strip().lower()
    while mode not in ("liter", "amount"):
        print("Type either 'liter' or 'amount' !!!")
        mode = input("Liter or Amount: ").strip().lower()

    if mode == "liter":
        prompt = f"How Many Liters of {name.lower()} are you buying ({price}/L): "
        liters = text_to_number(input(prompt))
        while liters is None or not is_valid_liters(liters):
            print(f"Liters must be between {MIN_LITERS} - {MAX_LITERS} !!!")
            liters = text_to_number(input(prompt))
        amount = calculate_amount(price, liters)
    else:
        prompt = f"How much {name} are you buying ({price}/L): "
        amount = text_to_number(input(prompt))
        while amount is None or not is_valid_amount(amount, price):
            print("Amount must be above a liter price !!!")
            amount = text_to_number(input(prompt))
        liters = calculate_liters(price, amount)

    print(make_receipt(name, amount, liters))
    print("Saving Transaction History......")
    record_transaction(transactions, name, amount, liters)


def main():
    transactions = []
    try:
        while True:
            print("\nWelcome to Amuludun Filling Station!")
            print("Available petroleum")
            print("    1. Buy Petroleum")
            print("    2. Show Transaction History")
            print("    3. Exit")
            choice = input("Enter operation: ").strip()
            if choice == "1":
                buy_petroleum(transactions)
            elif choice == "2":
                print(make_history(transactions))
            elif choice == "3":
                print("Goodbye!")
                return
            else:
                print("Invalid operation. Enter 1, 2 or 3 !!!")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()