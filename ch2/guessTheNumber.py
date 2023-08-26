import random

correctGuess = random.randint(1,20)
guess = -1
tries = 0
print('I am thinking of a number between 1 and 20.')
while (guess is not correctGuess):
    print('Take a guess.')
    guess = int(input())
    if(guess < correctGuess):
        print('Your guess is too low')
    if(guess > correctGuess):
        print('Your guess is too high')
    tries = tries + 1
print('Good job! You guessed my number in 4 guesses!')

