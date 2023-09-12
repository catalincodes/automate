import random, time, copy
WIDTH = 30
HEIGHT = 40

# Create list of cells
nextCells = []
for x in range(0, WIDTH):
    column = []
    for y in range(0, HEIGHT):
        if (random.randint(0, 1) == 0):
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
currentCells = copy.deepcopy(nextCells)

#Main Program Loop
while True:
    currentCells = copy.deepcopy(nextCells)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    #Display cells
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            print(currentCells[x][y] + ' ', end='')
        print('')

    #Calculate next step cells:
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):

            #Get neighbour coordinates
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH

            #Count living neighbours
            livNeighbours = 0
            if (currentCells[leftCoord][aboveCoord] == '#'): livNeighbours += 1
            if (currentCells[x][aboveCoord] == '#'): livNeighbours += 1
            if (currentCells[rightCoord][aboveCoord] == '#'): livNeighbours += 1
            if (currentCells[leftCoord][y] == '#'): livNeighbours += 1
            if (currentCells[rightCoord][y] == '#'): livNeighbours += 1
            if (currentCells[leftCoord][belowCoord] == '#'): livNeighbours += 1
            if (currentCells[x][belowCoord]) == '#': livNeighbours += 1
            if (currentCells[rightCoord][belowCoord] == '#'): livNeighbours += 1
            
            #Apply Conway Rules
            if (currentCells[x][y] == '#' and \
                    (livNeighbours == 2 or livNeighbours == 3)):
                nextCells[x][y] = '#'
            elif (currentCells[x][y] == ' ' and livNeighbours == 3):
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

    time.sleep(1)
#Main Program Loop
#Display cells
#Calculate next step
    #Get neighbours
    #Count living neigbours
    #Conway Rules (
    #   liv cells w/ 2-3 nei stay alive, 
    #   dead cells with 3 nei become alive, 
    #   dead)

