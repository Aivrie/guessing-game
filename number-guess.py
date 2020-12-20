''' 
Number Guessing game - A program in which the computer randomly chooses a number between 1-n

Rules:
* Everytime a user guesses wrong, his score is reduced and he gets a clue
* Clues can be multiples, divisions, factors and so on
'''

import random
import math

# Step 1: Computer generates random number between 1-10 (Value is a multiple of 2 (even number))

def random_number():
    even = []
    for elem in range(1, 10):
        if elem % 2 == 0:
            even.append(elem)
            computer = random.choice(even)
    return computer

# Step 2: Computer asks user to guess a number between 1-n. Computer gives user a hint (Computer takes in user's guess and compares it to its selected number)

def check_guess():
    print('Guess a number between 1-10. You have 3 tries (Hint: The value is an even number between 1-10)')
    guess = int(input('Enter number: '))
    
    value = random_number()
        
    if win(guess, value):
        return (1, guess, value)
    
    # Checks and clues for when user loses
    if guess < value:
        return (-1, guess, value)
    else:
        return (-1, guess, value)


# Step 3: Create win() helper function
def win(guess, value):
    if guess == value:
        return True
    return False
        
    
# Step 4:
#Play Best of game()
def best_of(n):
    player_wins = 0
    opponent_wins = 0
    wins_necessary = math.ceil(n/2)
    
    while (player_wins < wins_necessary and opponent_wins < wins_necessary):
        (result, guess, value) = check_guess()
        
        # Win
        if(result == 1):
            player_wins += 1
            print("You and the computer have chosen {}. You win\n".format(value))
        
        # Lose (low)
        elif ((result == -1) and (guess < value)):
            opponent_wins += 1
            print("Guess too low.")
            # print("You have chosen {} and the computer has chosen {}. You lose\n".format(guess, value))
            
        else:
            opponent_wins += 1
            print("Guess too high.")
            # print("You have chosen {} and the computer has chosen {}. You lose\n".format(guess, value))
            
    if (player_wins > opponent_wins):
        print("You have won the best out {} games. What a champ!".format(n))
    else:
        print("Unfortunately, the computer has won the best out {} games. Try again later".format(n))



#Initiate game
if __name__ == '__main__':
    best_of(3)
