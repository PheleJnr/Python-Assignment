father_age = int(input("Enter Father's current age 1-80: "))
son_age = int(input("Enter Son's current age 1-80: "))


if father_age == 2 * son_age:
    print("Father is already twice as old as his son.")
    exit() 

past_father = father_age
past_son = son_age
past_years = 0

while past_son >= 0:
    if past_father == 2 * past_son:
        print(str(past_years) + " years ago, father was twice as old as his son.")
        exit()  

    past_father -= 1
    past_son -= 1
    past_years += 1


future_father = father_age
future_son = son_age
future_years = 0

while True:
    future_father += 1
    future_son += 1
    future_years += 1

    if future_father == 2 * future_son:
       print("In " + str(future_years) + " years, father will be twice as old as his son.")
       break  