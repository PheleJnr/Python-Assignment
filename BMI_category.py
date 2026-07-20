weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)


if bmi < 18.5:
    category = "Underweight"

elif bmi <= 24.9:
    category = "Normal"

elif bmi <= 29.9:
    category = "Overweight"

else:
    category = "Obese"


print("Your BMI is:", round(bmi, 2))
print("Category:", category)