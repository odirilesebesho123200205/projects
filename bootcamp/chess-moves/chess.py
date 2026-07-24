
"""
"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

8  r n b q k b n r
7  p p p p p p p p
6  . . . . . . . .
5  . . . . . . . .
4  . . . . . . . .
3  . . . . . . . .
2  P P P P P P P P
1  R N B Q K B N R
   a b c d e f g h


pieces = [
    [r n b q k b n r],
    [p p p p p p p p],
    
    for list in pieces:
       
       print(" ".join(list))
    
    " ".join()
]

"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
, to_move, castling_rights, ep, hm, fm 
"""

def main():
    board = parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    display_board(board)
    print(generate_moves(board))

def parse_fen(fen):
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")
    pieces = [[]]
    for char in fen_pieces:
        if char.isdigit(): # we are checking if a character is a digit 
            pieces[-1].extend(["."] * int(char)) #the code is saying that if it is indeed a digit, it must 
        elif char == "/":
            pieces.append([])
        else:
            pieces[-1].append(char)

    return pieces

def generate_moves(board):
    return (
         knight_moves(board) +
         king_moves(board) +
         rook_moves(board) + 
         bishop_moves(board) +
         queen_moves(board)
    )

def knight_moves(board):
    """Returns number of legal moves a knight can make"""
    return -1

def king_moves(board):
    """Returns the number of legal moves a king can make"""
    return -1

def rook_moves(board):
    """Returns the number of legal moves a rook can make"""
    return -1

def bishop_moves(board):
    """Returns the number of legal moves a bishop can make"""
    return -1

def queen_moves(board):
    """Returns the number of legal queen"""
    return -1


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")

def display_board(board):
    """Prints the chess board"""
    for row in board:
            print(" ".join(row))

def is_in_board(location, board):
    """Determines whether a location is inside the board"""

main()