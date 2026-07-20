#collect string input from the user 
#use the if elif else selection statement
#print out the result


text = input("Enter a string: ")

if len(text) < 5:
    print("Short string")

elif len(text) <= 10:
    print("Medium string")

else:
    print("Long string")