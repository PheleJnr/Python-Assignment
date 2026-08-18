import random

def play_game():

    """Play one round of guess the number."""
    
    secret_number = random.randrange(1, 1001)
    
    guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))

    while guess != secret_number:
    
        if guess > secret_number:
        
            print('Too high. Try again.')
            
        else:
        
            print('Too low. Try again.')
            
        guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))

    print('Congratulations. You guessed the number!')

play_again = 'yes'

while play_again == 'yes':

    play_game()
    
    play_again = input('Play again? (yes/no): ')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
