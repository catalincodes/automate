def validateKeys(positions):
    for (index, item) in enumerate(positions):
        pos = item
        if len(pos) > 2: return False
        
        #validate the number of the position
        charOne = pos[0]
        if charOne.isdigit() is False\
                or int(charOne) > 8\
                or int(charOne) < 1:
            return False

        #validate the letter of the position
        charTwo = pos[1]
        if charTwo > 'h' or charTwo < 'a':
            return False

    return True

def validateColor(pieces):
    for (index, item) in enumerate(pieces):
        if (len(item) < 5): return False
        # print(item[0])
        if ((item[0] == 'w' or item[0] == 'b') is False): return False

    return True

def validateValues(pieces):
    if validateColor(pieces) is False: return False

    return True

def validatePiece(piece): 
    return (piece in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king'])

def getPiecesByColor(color, piecesList):
    firstChar = '';
    if (color == 'white'): firstChar = 'w'
    elif (color == 'black'): firstChar = 'b'
    else: return None

    resultList = []

    for (index, item) in enumerate(piecesList):
        if(item[0] == firstChar): resultList.append(item)

    return resultList

def validateChessPieces(pieces):
    if (len(pieces) > 16): return False
    if (len(list(filter(lambda p: p[1:] == 'pawn', pieces))) > 8): return False

    return True

def isValidChessBoard(board):
    positions = list(board.keys())

    # Validate Keys
    if (validateKeys(positions)) is False: return False

    pieces = list(board.values())
    # Validate Values
    
    print(pieces)
    if (validateValues(pieces)) is False: return False

    for (index, item) in enumerate(pieces):
        if(validatePiece(item[1:]) is False): return False

    whitePieces = getPiecesByColor('white', pieces)
    blackPieces = getPiecesByColor('black', pieces)
    
    print('white pieces: ', end='')
    for (index, item) in enumerate(whitePieces):
        print(item, end=', ')

    print('\nblack pieces: ', end='')
    for (index, item) in enumerate(blackPieces):
        print(item, end=', ')

    print('\n')

    if ( validateChessPieces(whitePieces) is False): return False
    #validate pieces
        #validate total 16 pieces
        #validate max 8 pawns
        #validate max 2 knights
        #validate max 2 bishops
        #validate max 2 rooks
        #validate one queen
        #validate one king
    return True

board = {
        '1a':'wpawn',
        '1b':'wpawn',
        '1c':'wpawn',
        '1d':'wpawn',
        '1e':'wpawn',
        '1f':'wpawn',
        '1g':'wpawn',
        '1h':'wpawn',
        '2a':'wrook',
        '2b':'bpawn'
        }
print(isValidChessBoard(board))
