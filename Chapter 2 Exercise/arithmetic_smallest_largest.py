#2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from the user. 
#Display the sum, average, product, smallest and largest of the numbers. 
#Note that each of these is a reduction in functional-style programming. 


#Answer: pseudocode
#collect three integer input from user 
#calculate the sum of the integers
#calculate the Average of the integers
#calculate the product of the integers 
#find the smallest of the three integers with if statement
#find the largest of the three integers with if statement
#print out the sum, average, product, smallest and largest


number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

sum_numbers = number1 + number2 + number3
average = sum_numbers / 3  
product = number1 * number2 * number3


smallest = number1
if number2 < smallest:
    smallest = number2
if number3 < smallest:
    smallest = number3

largest = number1
if number2 > largest:
    largest = number2
if number3 > largest:
    largest = number3

print("Sum:", sum_numbers)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)