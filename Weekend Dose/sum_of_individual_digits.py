def sum_of_individual_digits(number):

    total = 0

    while(number > 0):

        total = total + number % 10

        number = number // 10

    return total


number = int(input("Enter any integer of your choice: "))

print("The sum of indiviual digit is: ", sum_of_individual_digits(number))
