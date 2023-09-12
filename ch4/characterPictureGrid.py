grid= [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(len(grid))

for y in range(0, 6):
    for x in range(0, 8):
        if(x == 7):
            #print("grid["+str(x)+"]["+str(y)+"]")
            print(grid[x][y])
        else:
            #print("grid["+str(x)+"]["+str(y)+"]", end = '')
            print(grid[x][y], end = '')

