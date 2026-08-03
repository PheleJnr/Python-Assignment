def count_even(numbers):

    count = 0

    for value in numbers:

        if value % 2 == 0:

            count += 1

    return count


def count_odd(numbers):

    count = 0

    for value in numbers:

        if value % 2 == 1:

            count+= 1

    return count


def count_even_odd(numbers):

    evens = count_even(numbers)

    odds = count_odd(numbers)

    return evens, odds


numbers = {4, 5, 17, 20, 45, 50, 33, 23, 19, 15, 14}


print("The even numbers are: ", count_even(numbers))
print("The odd numbers are: ", count_odd(numbers))
print("The total counts of both even and odd numbers are: ", count_even_odd(numbers))
 
