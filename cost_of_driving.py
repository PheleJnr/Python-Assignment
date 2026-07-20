#collect input for distance to drive in miles
#collect input for fuel efficiency miles per gallon
#collect input for price per gallon 
#calculate the cost of the trip 
#print the result out.


distance = float(input("Enter the distance to drive in miles: "))

miles_per_gallon = float(input("Enter the fuel efficiency miles per gallon: "))

price_per_gallon = float(input("Enter the price per gallon: "))

cost = (distance / miles_per_gallon) * price_per_gallon

print("The cost of the trip is: $" + str(round(cost, 2)))