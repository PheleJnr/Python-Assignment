x = int(input("Enter Integer x: "))
y = int(input("Enter Integer y: "))

if x == 0 and y == 0:
    location = "Origin"

elif y == 0 and x != 0:
    location = "X-axis"

elif x == 0 and y != 0:
    location = "Y-axis"

elif x > 0 and y > 0:
    location = "Q1"

elif x < 0 and y > 0:
    location = "Q2"

elif x < 0 and y < 0:
    location = "Q3"

else:
    location = "Q4"

print("Location:", location)