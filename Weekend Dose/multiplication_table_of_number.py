def multiplication_table_of_number(number):

    for number in range (1, (number + 1)):

        for count in range (1, 11):

            print(f"{count} x {number} = {number * count}", end="\t ")
        print ()


number = int(input("Enter any number of your choice: "))

multiplication_table_of_number(number)

