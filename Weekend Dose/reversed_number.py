def reversed_number(number):

    reversed_value = 0

    while number > 0:

        reversed_value = reversed_value * 10 + number % 10

        number = number // 10

    return reversed_value


number = int(input("Enter a integer: "))

print("The reversed digits are: ", reversed_number(number))







