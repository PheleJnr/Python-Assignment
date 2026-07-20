#2.2 (What’s wrong with this code?) The following code should read an integer into the variable rating: rating = input('Enter an integer rating between 1 and 10')

#Answer:

The code doesn't have the data type for the user to input but then it prints out as a string '5'. The input() always return as a string so we need the int() to convert it back as an integer.

The right code would be:

rating = int(input('Enter an integer rating between 1 and 10'))

rating = 5