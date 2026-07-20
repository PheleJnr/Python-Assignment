#collect input for user age
#use the if elif statement to categorize depending on the user input
#print the result out


age = int(input("Enter your age: "))

if age < 13:
    print("You are a: Child")

elif age < 20:
    print("You are a: Teen")

else:
    print("You are an: Adult")