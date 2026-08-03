def sum_of_all_numbers(number):
   
    total = 0

    for count in range(1, (number +1)):

        total = total + count

    return total

number = int(input("Enter the number: "))
 
total = sum_of_all_numbers(number)

print("The sum of all numbers of a given number: ", total)

