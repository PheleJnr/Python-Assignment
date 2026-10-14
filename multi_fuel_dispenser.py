from datetime import date

FUELS = {
    1: ("Petrol", 650),
    2: ("Diesel", 720),
    3: ("Kerosene", 550),
    4: ("Gas", 480),
}
MIN_LITERS = 1
MAX_LITERS = 50
LINE = "=" * 37


def text_to_number(text):
    try:
        return float(text)
    except ValueError:
        return None


def is_valid_liters(liters):
    return MIN_LITERS <= liters <= MAX_LITERS


def is_valid_amount(amount, price):
    return price < amount < float("inf")


def calculate_amount(price, liters):
    return round(price * liters, 2)


def calculate_liters(price, amount):
    return round(amount / price, 2)


def format_number(value):
    return f"{value:.2f}".rstrip("0").rstrip(".")


def make_receipt(product, amount, liters):
    return "\n".join([
        "Customers Transaction Receipt",
        LINE,
        f"=      Product : {product}".ljust(36) + "=",
        f"=      Amount  : #{format_number(amount)}".ljust(36) + "=",
        f"=      Liters  : {format_number(liters)}L".ljust(36) + "=",
        "=      Thank you For your Petronage".ljust(36) + "=",
        LINE,
    ])


def record_transaction(transactions, product, amount, liters):
    transaction = {
        "product": product,
        "amount": amount,
        "liters": liters,
        "date": date.today().strftime("%d/%m/%Y"),
    }
    transactions.append(transaction)
    return transaction


def make_history(transactions):
    if not transactions:
        return "No transactions yet."
    transaction_boxes = []
    for item in transactions:
        transaction_boxes.append("\n".join([
            LINE,
            f"=      Product : {item['product']}".ljust(36) + "=",
            f"=      Amount  : #{format_number(item['amount'])}".ljust(36) + "=",
            f"=      Liters  : {format_number(item['liters'])}L".ljust(36) + "=",
            f"=      Date    : {item['date']}".ljust(36) + "=",
            LINE,
        ]))
    return "All Transactions\n" + "\n\n".join(transaction_boxes)