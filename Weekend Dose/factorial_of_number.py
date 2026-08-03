def factorial_of_number(number):

    total = 1

    for count in range(1, (number + 1)):

        total = total * count

    return total


number = int(input("Enter a Factorial number: ")) 

total = factorial_of_number(number) 

print("The Factorial of unknown number is: ", total)




