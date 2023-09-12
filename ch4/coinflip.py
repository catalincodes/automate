import random

def getToss():
    result = random.randint(0,1)
    if (result == 0): return 'H'
    else: return 'T'

def getHundredTosses():
    listTosses = []
    for _ in range(0, 100):
        tossResult = getToss()
        listTosses.append(tossResult)
    return listTosses

def calculateStreaks(lst):
    numStreaks = 0
    length = len(lst)
    for i in range (5, length):
        if(lst[i] == lst[i - 1] == lst[i - 2] == lst[i - 3] == lst[i - 4] == lst[i - 5]):
            numStreaks += 1
    return numStreaks


numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listTosses = getHundredTosses()

    # Code that checks if there is a streak of 6 heads or tails in a row.
    currNumberOfStreaks = calculateStreaks(listTosses)
    numberOfStreaks += currNumberOfStreaks
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
