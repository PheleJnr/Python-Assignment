import random


def generate_numbers():
    
    return (random.randint(1, 9), random.randint(1, 9))


def multiplication():

    number1, number2 = generate_numbers()
    
    answer = number1 * number2

    while True:
    
        user_response = input(f"How much is {number1} times {number2}: ")

        if int(user_response) == answer:
                
            print("Very good!")
                    
            break
                    
        else:
                
            print("No. Please try again.")

print(multiplication())

