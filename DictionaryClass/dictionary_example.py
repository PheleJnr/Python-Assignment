


new_dictionary = {"key": "value",

                  "key2": "value2",

                  "key3": ["value3", "value4", 78, 90.9, True, False],

                }
print(new_dictionary)




new_dictionary["key6"] = "changed value6"
print(new_dictionary)

new_dictionary["key3"] = "changed value7"
print(new_dictionary)

del new_dictionary["key2"]
print(new_dictionary)


roman_numeral = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}

for key in roman_numeral:
    print(roman_numeral[key])
    print(f"key: {key} \t Value: {[roman_numeral[key]]}")


for item in roman_numeral.items():
    print(item)
    print(f"key: {item[0]} \t Value: {item[1]}")

print(roman_numeral.items())
print(roman_numeral.keys())
print(roman_numeral.values())
print(tuple(roman_numeral.keys()))
print(tuple(roman_numeral.values()))

# Retrieval of items
print(roman_numeral[6])
print(roman_numeral.get(16, "key not found"))

# Methods in Dictionary

roman_numeral.update({11:"XI", 12:"XII"})
print(roman_numeral)

figure = roman_numeral.pop(2)

roman_numeral.popitem()

# roman_numeral.clear()
# print(roman_numeral)

new_number = {}.fromkeys([15,16,17,18,19,20], "DL")
print(new_number)


worker_one = {"name": "Musa", "age": 25, "gender":"Male"}
worker_two = {"name": "John", "age": 25, "gender":"Male"}
worker_three = {"age":25, "gender": "Male", "name": "Musa"}

print(worker_one == worker_two)
print(worker_one == worker_three)
print(worker_two == worker_three)

new_dict ={key : roman_numeral[key] for key in roman_numeral}
new_dict = {key : value for key, value in roman_numeral.items()}
new_dict = {key : value for key, value in roman_numeral.items() if value != "V"}

print(new_dict)
print(new_dict)
print(new_dict)


#SET OPERATORS

# new_range = list(range(10)) + list(range(5))
# print(new_range)
#
# set(new_range)
# print(new_range)



new_set = set()
print(new_set)

new_set.add("Kemi")
new_set.add("Honour")
new_set.add("Elder")
new_set.add("Kemi")
print(new_set)

new_set.remove("Kemi")
print(new_set)

new_set.discard("Honour")
print(new_set)
