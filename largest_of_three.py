a = int(input("Enter first integer A: "))
b = int(input("Enter second integer B: "))
c = int(input("Enter third integer C: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("The largest number is:", largest)