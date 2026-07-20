#collect number from the user 
#use the if elif else selection statement 
#print the result out 


number = int(input("Enter a number: "))

if number % 5 == 0 and number % 3 == 0:
    print(number, "is divisible by both 5 and 3")

elif number % 5 == 0:
    print(number, "is divisible by 5 but NOT by 3")

elif number % 3 == 0:
    print(number, "is divisible by 3 but NOT by 5")

else:
    print(number, "is NOT divisible by either 5 or 3")