def repeat_positive_integer(number):

    counter = 0

    while (number > 1):

        if (number % 2 == 0):
            number = number // 2

        else: 
            number = ((number * 3) + 1)
        
        counter = counter + 1


    return counter
    

number = int(input("Enter a positive number: "))

print("The number of times it takes to get to 1: ", repeat_positive_integer(number), "steps")









