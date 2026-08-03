def apply_discount(item_name, original_price, promo_code):

    if promo_code == "SAVE10":
        discount = 0.10

    elif promo_code == "HALFOFF":
        discount = 0.50

    else:
        discount = 0

    discounted_price = original_price - (original_price * discount)

    return discounted_price


item_name = input("Enter an item: ")

original_price = int(input("Enter the Price: "))

promo_code = input("Enter the promo code: ")


print(apply_discount(item_name, original_price, promo_code))





