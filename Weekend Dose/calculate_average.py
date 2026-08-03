def calculate_average():

    total = 0

    for _ in range(10):

        number = int(input("Enter a number: "))
        
        total = total + number

    average = total / 10

    return average


result = calculate_average()

print("The average is:", result)

