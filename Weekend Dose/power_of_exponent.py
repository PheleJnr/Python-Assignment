def power_of_exponent(base, exponent):

    result = 1

    for _ in range(exponent):

        result = result * base
    
    return result


base = float(input("Enter a number: "))
exponent = int(input("Enter the exponent value: "))

result = power_of_exponent(base, exponent)
print(result)




