def guess_the_number():

    secret_number = 42

    guess_number = int(input("Guess a number between 1 and 100: "))
    
    while guess_number != secret_number:

        if guess_number > secret_number:

            print("Too high, Try again.")

        else:

            print("Too low, Try again.")

        guess_number = int(input("Try guessing again: "))
    
    print("Correct, You got it.")

guess_the_number()
