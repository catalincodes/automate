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

def validateNumChessPiecesOfType(pieces, pieceType, maxPieces):
    filteredPieces = filter(lambda p:p[1:] == pieceType, pieces)
    specificTypePieces = list(filteredPieces)
    if (len(specificTypePieces) > maxPieces): return False

    return True

def validateChessPieces(pieces):
    if (len(pieces) > 16): return False

    # Validates having only 8 pawns
    if (validateNumChessPiecesOfType(pieces, 'pawn', 8) is False): return False

    # Validates having only 2 rooks
    if (validateNumChessPiecesOfType(pieces, 'rook', 2) is False): return False

    # Validates having only 2 knights
    if (validateNumChessPiecesOfType(pieces, 'knight', 2) is False): return False

    # Validates having only 2 bishops
    if (validateNumChessPiecesOfType(pieces, 'bishop', 2) is False): return False

    # Validates having only 1 queen
    if (validateNumChessPiecesOfType(pieces, 'queen', 1) is False): return False

    # Validates having only 1 king
    if (validateNumChessPiecesOfType(pieces, 'king', 1) is False): return False

    return True

def isValidChessBoard(board):
    positions = list(board.keys())

    # Validate Keys
    if (validateKeys(positions)) is False: return False

    pieces = list(board.values())
    # Validate Values
    
    if (validateValues(pieces)) is False: return False

    for (index, item) in enumerate(pieces):
        if(validatePiece(item[1:]) is False): return False

    whitePieces = getPiecesByColor('white', pieces)
    blackPieces = getPiecesByColor('black', pieces)
    
    if ( validateChessPieces(whitePieces) is False): return False
    if ( validateChessPieces(blackPieces) is False): return False
    
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
        '2b':'wrook',
        '2c':'wknight',
        '2d':'wknight',
        '2e':'wbishop',
        '2f':'wbishop',
        '2g':'wqueen',
        '2h':'wking',
        '3a':'bpawn',
        '3b':'bpawn',
        '3c':'bpawn',
        '3d':'bpawn',
        '3e':'bpawn',
        '3f':'bpawn',
        '3g':'bpawn',
        '3h':'bpawn',
        '4a':'brook',
        '4b':'brook',
        '4c':'bknight',
        '4d':'bknight',
        '4e':'bbishop',
        '4f':'bbishop',
        '4g':'bqueen', 
        '4h':'bking'
        }

result = isValidChessBoard(board)
if (result is True): print('Valid chess board!')
else: print('Not a valid chess board!')
