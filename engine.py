

# print("♔♕♖♗♘♙□■♚♛♜♝♞♟")

# EARLY TESTS

# empty board
# print("  a b c d e f g h  \n8 ■ □ ■ □ ■ □ ■ □ 8\n7 □ ■ □ ■ □ ■ □ ■ 7\n6 ■ □ ■ □ ■ □ ■ □ 6\n5 □ ■ □ ■ □ ■ □ ■ 5\n4 ■ □ ■ □ ■ □ ■ □ 4\n3 □ ■ □ ■ □ ■ □ ■ 3\n2 ■ □ ■ □ ■ □ ■ □ 2\n1 □ ■ □ ■ □ ■ □ ■ 1\n  a b c d e f g h  ")
# coltitle = "  a b c d e f g h  \n"
# row8 = "8 ■ □ ■ □ ■ □ ■ □ 8\n"
# row7 = "7 □ ■ □ ■ □ ■ □ ■ 7\n"
# row6 = "6 ■ □ ■ □ ■ □ ■ □ 6\n"
# row5 = "5 □ ■ □ ■ □ ■ □ ■ 5\n"
# row4 = "4 ■ □ ■ □ ■ □ ■ □ 4\n"
# row3 = "3 □ ■ □ ■ □ ■ □ ■ 3\n"
# row2 = "2 ■ □ ■ □ ■ □ ■ □ 2\n"
# row1 = "1 □ ■ □ ■ □ ■ □ ■ 1\n"
# rowsall = row8+row7+row6+row5+row4+row3+row2+row1
# print(coltitle+rowsall+coltitle)

# # starting board
# row8 = "8 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 8\n"
# row7 = "7 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 7\n"
# row6 = "6 ■ □ ■ □ ■ □ ■ □ 6\n"
# row5 = "5 □ ■ □ ■ □ ■ □ ■ 5\n"
# row4 = "4 ■ □ ■ □ ■ □ ■ □ 4\n"
# row3 = "3 □ ■ □ ■ □ ■ □ ■ 3\n"
# row2 = "2 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 2\n"
# row1 = "1 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 1\n"
# rowsall = row8+row7+row6+row5+row4+row3+row2+row1
# print(coltitle+rowsall+coltitle)


# PIECE ASSIGNMENT

# white square = 0
# black square = 1

# white pawn = 2
# black pawn = 3

# white rook = 4
# black rook = 5
 
# white knight = 6
# black knight = 7

# white bishop = 8
# black bishop = 9

# white queen = 10
# black queen = 11

# white king = 12
# black king = 13

startboard = [
    [5, 7, 9, 11, 13, 9, 7, 5,],
    [3, 3, 3, 3,  3,  3, 3, 3,],
    [0, 1, 0, 1,  0,  1, 0, 1,],
    [1, 0, 1, 0,  1,  0, 1, 0,],
    [0, 1, 0, 1,  0,  1, 0, 1,],
    [1, 0, 1, 0,  1,  0, 1, 0,],
    [2, 2, 2, 2,  2,  2, 2, 2,],
    [4, 6, 8, 10, 12, 8, 6, 4,],
    ]

def assign_figurine(num:int) -> str:
    """
    Transforms a figurine number into the figurine unicode.
    """
    match num:
        case 0: return "■"
        case 1: return "□"
        case 2: return "♟"
        case 3: return "♙"
        case 4: return "♜"
        case 5: return "♖"
        case 6: return "♞"
        case 7: return "♘"
        case 8: return "♝"
        case 9: return "♗"
        case 10: return "♛"
        case 11: return "♕"
        case 12: return "♚"
        case 13: return "♔"


def print_board(board:list):
    """
    Prints the board from the input board list.
    """
    # works

    coltitle = "  a b c d e f g h  \n"
    rowstring = coltitle

    for i_row in range(8):
        rowstring += f"{8-i_row} "
        for j_col in range(8):
            rowstring = rowstring + f"{assign_figurine(board[i_row][j_col])} "
        rowstring += f"{8-i_row}\n"

    rowstring += coltitle
    print(rowstring)


def check_square_colour(row:int, column:int) -> int:
    """
    Checks whether the provided square is black or white.
    Returns 0 for white and 1 for black.
    """
    if row%2 == column%2:
        return 0
    else:
        return 1
    

def update_move(board:list, movestring:str) -> list:
    """
    Updates the board after a move.
    UNAMBIGUOUS algebraic notation is needed: 
    K king, Q queen, R rook, B bishop, N knight, P pawn.
    Examples: B1f6a.
    Do not add x in case of capture.
    """
    movelist = list(movestring)
    if movelist[3]=='x':
        del movelist[3]

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])

    start_colour = check_square_colour(start_row, start_col)
    start_piece_num = board[start_row][start_col]

    board[start_row][start_col] = start_colour
    board[end_row][end_col] = start_piece_num

    return board


def check_pawn_move(board:list, movestring:str) -> bool:
    """
    Check whether the pawn move is valid.
    Returns True or False.
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        capture = True
        del movelist[3]
    else:
        capture = False
    
    # check whether the piece is a pawn
    if movelist[0]!='P':
        raise ValueError("Error: Check pawn move piece is not pawn.")
    
    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])
    
    piece_num = board[start_row][start_col]
    if piece_num!=2 and piece_num!=3:
        raise ValueError("Error: Attempted pawn moved is not a pawn.")
    
    # check which pawn
    if piece_num==2:
        # white pawn
        if capture:
            # check whether there is black piece at the end
            if board[end_row][end_col]>1 and board[end_row][end_col]%2==1:
                return (start_row-end_row)==(end_col-start_col)%2==1
            else:
                return False
        else:
            # two moves available if and only if start sqaure
            if start_row==6: #on board it is 2
                return (((start_row-end_row)==1 or (start_row-end_row)==2) and (end_col-start_col)==0)
            else:
                return ((start_row-end_row)==1 and (end_col-start_col)==0)
    else: 
        # black pawn
        if capture:
            # check whether there is white piece at the end
            if board[end_row][end_col]>1 and board[end_row][end_col]%2==0:
                return (end_row-start_row)==(end_col-start_col)%2==1
            else:
                return False
        else:
            # two moves available if and only if start sqaure
            if start_row==1: #on board it is 7
                return (((end_row-start_row)==1 or (end_row-start_row)==2) and (end_col-start_col)==0)
            else:
                return ((end_row-start_row)==1 and (end_col-start_col)==0)


def check_rook_move(board:list, movestring:str) -> bool:
    """
    Check whether the rook move is valid.
    Returns True or False.
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        capture = True
        del movelist[3]
    else:
        capture = False
    
    # check whether the piece is a rook
    if movelist[0]!='R':
        raise ValueError("Error: Check rook move piece is not rook.")
    
    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])
    
    piece_num = board[start_row][start_col]
    if piece_num!=4 and piece_num!=5:
        raise ValueError("Error: Attempted rook moved is not a rook.")
    

    if capture:
        # check whether there is opponent piece at the end
        if board[end_row][end_col]>1 and board[end_row][end_col]%2!=piece_num%2:
            return (start_col-end_col)==0 or (start_row-end_row)==0
        else:
            return False
    else:
        return (start_col-end_col)==0 or (start_row-end_row)==0


def check_knight_move(board:list, movestring:str) -> bool:
    """
    Check whether the knight move is valid.
    Returns True or False.
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        capture = True
        del movelist[3]
    else:
        capture = False
    
    # check whether the piece is a knight
    if movelist[0]!='N':
        raise ValueError("Error: Check knight move piece is not knight.")
    
    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])
    
    piece_num = board[start_row][start_col]
    if piece_num!=6 and piece_num!=7:
        raise ValueError("Error: Attempted knight moved is not a knight.")
    
    if capture:
        # check whether there is opponent piece at the end
        if board[end_row][end_col]>1 and board[end_row][end_col]%2!=piece_num%2:
            return (
                (abs(start_col-end_col)==1 and abs(start_row-end_row)==2) or
                (abs(start_col-end_col)==2 and abs(start_row-end_row)==1)
            )
        else:
            return False
    else:
        return (
                (abs(start_col-end_col)==1 and abs(start_row-end_row)==2) or
                (abs(start_col-end_col)==2 and abs(start_row-end_row)==1)
            )
    
def check_bishop_move(board:list, movestring:str) -> bool:
    """
    Check whether the bishop move is valid.
    Returns True or False.
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        capture = True
        del movelist[3]
    else:
        capture = False
    
    # check whether the piece is a knight
    if movelist[0]!='B':
        raise ValueError("Error: Check bishop move piece is not bishop.")
    
    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])
    
    piece_num = board[start_row][start_col]
    if piece_num!=8 and piece_num!=9:
        raise ValueError("Error: Attempted bishop moved is not a bioshop.")
    
    if capture:
        # check whether there is opponent piece at the end
        if board[end_row][end_col]>1 and board[end_row][end_col]%2!=piece_num%2:
            return abs(start_row-end_row)==abs(start_col-end_col)
        else:
            return False
    else:
        return abs(start_row-end_row)==abs(start_col-end_col)


def check_queen_move(board:list, movestring:str) -> bool:
    """
    Check whether the queen move is valid.
    Returns True or False.
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        capture = True
        del movelist[3]
    else:
        capture = False
    
    # check whether the piece is a knight
    if movelist[0]!='Q':
        raise ValueError("Error: Check queen move piece is not queen.")
    
    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])
    
    piece_num = board[start_row][start_col]
    if piece_num!=10 and piece_num!=11:
        raise ValueError("Error: Attempted queen moved is not a queen.")
    
    if capture:
        # check whether there is opponent piece at the end
        if board[end_row][end_col]>1 and board[end_row][end_col]%2!=piece_num%2:
            return (
                (abs(start_col-end_col)==1 and abs(start_row-end_row)==2) or
                (abs(start_col-end_col)==2 and abs(start_row-end_row)==1) or
                (abs(start_row-end_row)==abs(start_col-end_col))
            )
        else:
            return False
    else:
        return (
                (abs(start_col-end_col)==1 and abs(start_row-end_row)==2) or
                (abs(start_col-end_col)==2 and abs(start_row-end_row)==1) or
                (abs(start_row-end_row)==abs(start_col-end_col))
            )


def check_king_move(board:list, movestring:str) -> bool:
    """
    Check whether the king move is valid.
    Returns True or False.
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        capture = True
        del movelist[3]
    else:
        capture = False
    
    # check whether the piece is a knight
    if movelist[0]!='K':
        raise ValueError("Error: Check king move piece is not king.")
    
    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])
    
    piece_num = board[start_row][start_col]
    if piece_num!=12 and piece_num!=13:
        raise ValueError("Error: Attempted king moved is not a king.")
    
    if capture:
        # check whether there is opponent piece at the end
        if board[end_row][end_col]>1 and board[end_row][end_col]%2!=piece_num%2:
            return abs(start_col-end_col)<=1 and abs(start_row-end_row)<=1
        else:
            return False
    else:
        return abs(start_col-end_col)<=1 and abs(start_row-end_row)<=1


def check_piece_has_moved(movestring:str) -> bool:
    """
    Check that the starting and end positions are not equal.
    """
    movelist = list(movestring)
    if movelist[3]=='x':
        del movelist[3]

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])

    return start_col!=end_col or start_row!=end_row


def check_correct_formatting_unambig(movestring:str) -> bool:
    """
    Check whether the unambiguous movestring is
    correctly formatted. Ex.: "R1hx7h".
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        del movelist[3]

    if len(movelist)!=5:
        return False

    figurines = ['P', 'R', 'N', 'B', 'Q', 'K']
    rows = ['8', '7', '6', '5', '4', '3', '2', '1']
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    figurine_bool = movelist[0] in figurines
    row_bool = (movelist[1] in rows) and (movelist[3] in rows)
    col_bool = (movelist[2] in cols) and (movelist[4] in cols)

    if figurine_bool and row_bool and col_bool:
        return True
    else:
        return False


def check_piece_matches(board:list, movestring:str) -> bool:
    """
    Check whether the piece in the move matches
    the piece on the board.
    """
    movelist = list(movestring)

    if movelist[3]=='x':
        del movelist[3]

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    
    piece_on_board = board[start_row][start_col]
    if piece_on_board%2==1:
        piece_on_board -= 1

    match movelist[0]:
        case 'P': return piece_on_board==2
        case 'R': return piece_on_board==4
        case 'N': return piece_on_board==6
        case 'B': return piece_on_board==8
        case 'Q': return piece_on_board==10
        case 'K': return piece_on_board==12


def check_obstruction_pawn(board:list, movestring:str) -> bool:
    """
    Assume move is normally allowed.
    Check whether the pawn move is (not) obstructed.
    Does not include capture in this case: returns True.
    """
    movelist = list(movestring)
    if movelist[3]=='x':
        return True

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])

    match end_row-start_row:
        case -2: return board[start_row-1][start_col]<2 and board[end_row][start_col]<2
        case -1: return board[end_row][start_col]<2
        case  1: return board[end_row][start_col]<2
        case  2: return board[start_row+1][start_col]<2 and board[end_row][start_col]<2


def check_obstruction_rook(board:list, movestring:str) -> bool:
    """
    Assume move is normally allowed.
    Check whether the rook move is (not) obstructed.
    """
    movelist = list(movestring)
    if movelist[3]=='x':
        del movelist[3]

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])

    statement = True
    if start_row!=end_row:
        delta = end_row-start_row
        myrange = range(1, delta) if delta>0 else range(delta, 0)
        
        for i in myrange:
            statement = statement and board[start_row+i][start_col]<2
    else:
        delta = end_col-start_col
        myrange = range(1, delta) if delta>0 else range(delta, 0)
        
        for i in myrange:
            statement = statement and board[start_row][start_col+i]<2

    return statement
    


def check_obstruction_bishop(board:list, movestring:str) -> bool:
    """
    Assume move is normally allowed.
    Check whether the bishop move is (not) obstructed.
    """
    movelist = list(movestring)
    if movelist[3]=='x':
        del movelist[3]

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])

    statement = True
    if end_col>start_col:
        delta = end_row-start_row
        myrange = range(1, delta) if delta>0 else range(delta, 0)
        
        for i in myrange:
            statement = statement and board[start_row+i][start_col+abs(i)]<2
    else:
        delta = end_row-start_row
        myrange = range(1, delta) if delta>0 else range(delta, 0)
        
        for i in myrange:
            statement = statement and board[start_row+i][start_col-abs(i)]<2

    return statement


def check_obstruction_queen(board:list, movestring:str) -> bool:
    """
    Assume move is normally allowed.
    Check whether the queen move is (not) obstructed.
    """
    movelist = list(movestring)
    if movelist[3]=='x':
        del movelist[3]

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])

    if start_col==end_col or start_row==end_row:
        return check_obstruction_rook(board,movestring)
    else:
        return check_obstruction_bishop(board,movestring)



def check_move(board:list,movestring:str,col:int) -> bool:
    """
    Check whether the move is allowed.
    Col corresponds to which player is moving
    """
    if not check_correct_formatting_unambig(movestring):
        print("Move is not correctly formatted.")
        return False

    if not check_piece_has_moved(movestring):
        print("Invalid move. Piece has not moved.")
        return False
    
    if not check_piece_matches(board,movestring):
        print("Invalid move. Piece on the board is different from that in move.")
        return False
    
    movelist = list(movestring)

    if movelist[3]=='x':
        capture = True
        del movelist[3]
    else:
        capture = False

    start_col = ord(movelist[2])-97
    start_row = 8-int(movelist[1])
    end_col = ord(movelist[4])-97
    end_row = 8-int(movelist[3])

    if capture and board[end_row][end_col]%2==board[start_row][start_col]%2:
        print("Invalid move. Cannot capture your own piece.")
        return False
    
    if board[start_row][start_col]%2!=col:
        print("Invalid move. Not your piece.")
        return False
    
    piece_type = board[start_row][start_col]
    if piece_type%2==1:
        piece_type -= 1

    match piece_type:
        case 0:  return False # is not a piece
        case 2:  return check_obstruction_pawn(board,movestring) if check_pawn_move(board,movestring) else False
        case 4:  return check_obstruction_rook(board,movestring) if check_rook_move(board,movestring) else False
        case 6:  return check_knight_move(board,movestring)
        case 8:  return check_obstruction_bishop(board,movestring) if check_bishop_move(board,movestring) else False
        case 10: return check_obstruction_queen(board,movestring) if check_queen_move(board,movestring) else False
        case 12: return check_king_move(board,movestring)


myboard = startboard
print_board(myboard)

turncount = 0
turn = ""
while True:
    if turncount%2==0:
        turn = "White's"
    else:
        turn = "Black's"
    
    print("Chess game begun. End the game by entering END.")

    print(f"{turn} turn. Enter move:")
    move = input()
    if move=="END":
        break

    if check_move(myboard, move, turncount%2):
        myboard = update_move(myboard,move)
        print_board(myboard)
        
        turncount += 1
        continue
    else:
        print("Illegal move. Try again.")
        continue

    break



# move = "P2d4d"
# print(check_move(myboard,move))
# myboard = update_move(myboard,move)
# print_board(myboard)

# move = "P2e4e"
# print(check_move(myboard,move))
# myboard = update_move(myboard,move)
# print_board(myboard)

# move = "B1f4c"
# print(check_move(myboard,move))
# myboard = update_move(myboard,move)
# print_board(myboard)

# move = "Q1d5h"
# print(check_move(myboard,move))
# myboard = update_move(myboard,move)
# print_board(myboard)




    


