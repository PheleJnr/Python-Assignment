import random

def play_game():

    """Play one round of guess the number, tracking the number of guesses."""
    
    secret_number = random.randrange(1, 1001)
    guess_count = 0

    guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
    guess_count += 1

    while guess != secret_number:
    
        if guess > secret_number:
        
            print('Too high. Try again.')
            
        else:
        
            print('Too low. Try again.')
            
        guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
        guess_count += 1


    print('Congratulations. You guessed the number!')
    
    print(f'You guessed the number in {guess_count} guesses.')


    if guess_count <= 10:
    
        print('Either you know the secret or you got lucky!')
        
    else:
    
        print('You should be able to do better!')
        
yes
play_again = 'yes'


while play_again == 'yes':

    play_game()
    
    play_again = input('Play again? (yes/no): ')
