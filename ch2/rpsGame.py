import random, sys

# Initialization
print('ROCK, PAPER, SCISSORS')
choice = ''
wins = 0
losses = 0
ties = 0

while(choice != 'q'):
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    choice = input()
    
    # Player Input
    humanChoice = ''
    if (choice == 'r'): humanChoice = 'ROCK'
    if (choice == 'p'): humanChoice = 'PAPER'
    if (choice == 's'): humanChoice = 'SCISSORS'
    if (choice == 'q'): sys.exit()
    print(humanChoice + ' versus...')
    
    # Computer "Input" (via Random) 
    computerChoice = ''
    cChoice = random.randint(1,3)
    if (cChoice == 1): computerChoice = 'ROCK'
    if (cChoice == 2): computerChoice = 'PAPER'
    if (cChoice == 3): computerChoice = 'SCISSORS'
    print(computerChoice)

    # human - Rock
    if (humanChoice == 'ROCK'):
        if(computerChoice == 'ROCK'):
            ties = ties + 1
            print('It is a tie!')
        if(computerChoice == 'PAPER'):
            losses = losses + 1
            print('You lose!')
        if(computerChoice == 'SCISSORS'):
            wins = wins + 1
            print('You win!')

    # human - Paper
    if (humanChoice == 'PAPER'):
        if(computerChoice == 'PAPER'):
            ties = ties + 1
            print('It is a tie!')
        if(computerChoice == 'SCISSORS'):
            losses = losses + 1
            print('You lose!')
        if(computerChoice == 'ROCK'):
            wins = wins + 1
            print('You win!')

    # human - Scissors
    if (humanChoice == 'SCISSORS'):
        if(computerChoice == 'SCISSORS'):
            ties = ties + 1
            print('It is a tie!')
        if(computerChoice == 'ROCK'):
            losses = losses + 1
            print('You lose!')
        if(computerchoice == 'PAPER'):
            wins = wins + 1
            print('You win!')

