#collect input for the day number
#use the match selection statement 
#print the result  


day_number = int(input("Enter a day number (1-7): "))

match day_number:
    case 1: day_name = "Sunday"
    case 2: day_name = "Monday"
    case 3: day_name = "Tuesday"
    case 4: day_name = "Wednesday"
    case 5: day_name = "Thursday"
    case 6: day_name = "Friday"
    case 7: day_name = "Saturday"
    case _: day_name = "Invalid day number"

print("Day:", day_name)