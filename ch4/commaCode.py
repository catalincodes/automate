def getInput():
    userInput = ' '
    listWords = []
    print('Please enter the words you want to add to the list. A blank entry will end the list')
    while(userInput != ''):
        userInput = input()
        if (userInput != ''): listWords.append(userInput)
    return listWords

def convertToPhrase(listWords):
    numWords = len(listWords)
    if (numWords == 0): return 'You need to provide at least one word.'

    phrase = ''
    for (index, item) in enumerate(listWords):
        if(index == 0): phrase += item
        if(index != 0 and index < numWords - 1): phrase+= (', ' + item)
        if(index == numWords - 1): phrase += (' and ' + item)

    return phrase


listWords = getInput()
phrase = convertToPhrase(listWords)
print(phrase)

