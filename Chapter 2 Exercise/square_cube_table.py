#2.8 (Table of Squares and Cubes) Write a script that calculates the squares and #cubes of the numbers from 0 to 5. 
#Print the resulting values in table format, as shown below. 
#Use the tab escape sequence to achieve the three-column output.

#number square cube
#0 0 0
#1 1 1
#2 4 8
#3 9 27
#4 16 64
#5 25 125


#Answer: pseudocode

#first print the table using the tab to space the strings of number, square and cube
#Use the for loop for iteration for 0 - 6
#Calculate for the square 
#Calculate for the cube also
#Then print the result in tabular format


print("number\tsquare\tcube")

for number in range(0, 6):

    square = number * number

    cube = number * number * number

    print(number, square, cube, sep="\t")