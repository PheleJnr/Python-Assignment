#collect input for the take off speed (v)
#collect input for the acceleration (a)
#calculate for the length of minimum runway  
#print the result out


speed = float(input("Enter the take off speed (v) in meters/seconds: "))

acceleration = float(input("Enter the acceleration (a) in meters/second: "))

length = (speed * speed) / (2 * acceleration)

print ("The minimum runway length for this airplane is: ", round(length, 2), "meters")