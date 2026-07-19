totalBill = float(input("Enter total bill amount: "))
membership = input("Are you a member (yes/no): ")

discount = 0.0
finalAmount = totalBill
message = ""

if totalBill >= 1000 and membership == "yes":
    discount = totalBill * 0.10
    finalAmount = totalBill - discount
    message = "10% member discount applied!"

elif totalBill >= 1000:
    discount = totalBill * 0.05
    finalAmount = totalBill - discount
    message = "5% non-member discount applied!"

else:
    message = "No discount applied."

print("Original bill: $" + str(totalBill))
print("Discount: $" + str(discount))
print("Final amount: $" + str(finalAmount))
print(message)