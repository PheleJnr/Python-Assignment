def prime_number_checker(number):

    is_prime = True

    for divisor in range(2, number):

        if number % divisor == 0:

            is_prime = False

    return is_prime

def prime_number_count(number):

    for counter in range(2, number + 1):

        if prime_number_checker(counter):

            print(counter)


number = int(input("Enter a number: "))

print (prime_number_checker(number))

prime_number_count(number)
















