#print the table header
#use the for loop for iteration 1 to 5
#calculate b as a + 1
#calculate the result as a raised to the power of b
#print out the result


print("a\tb\tpow(a, b)")


for a in range(1, 6):
    b = a + 1
    result = int(a ** b)  

    print(str(a) + "\t" + str(b) + "\t" + str(result))