def count_multiples_of_number(number):

    count = 0

    for value in range(1, 101):

        if value % number == 0:

            count += 1

    return count


number = int(input("Enter a valid number between 1 - 100: "))

print("The number of count of a multiple of number from 1 - 100 is: ", count_multiples_of_number(number)) 

