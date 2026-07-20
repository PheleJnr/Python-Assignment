#2.11 (Separating the Digits in an Integer) Write a script that inputs a five-digit integer from the user. 
#Separate the number into its individual digits. 
#Print them separated by three spaces each. 
#For example, if the user types in the number 42339, the script should print
#4 2 3 3 9


#Answer: pseudocode
#collect five digit integers input from the user 
#seperate the numbers using the floor divisor and remainder
#print the result out 


number = int(input("Enter a five-digit integer: "))

digit1 = (number // 10000) % 10
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10


print(digit1, " ", digit2, " ", digit3, " ", digit4, " ", digit5, sep="")