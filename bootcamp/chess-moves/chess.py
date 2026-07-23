
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

def parse_fen(fen):
    fen_pieces= fen.split(" ")
    pieces = [[]]
    for char in fen:
        if char.isdigit(): # we are checking if a character is a digit 
            pieces[-1].extend(["."] * int(char)) #the code is saying that if it is indeed a digit, it must 
        elif char == "/":
            pieces.append([])
        else:
            pieces[-1].append(char)

    
    for row in pieces:
        print(" ".join(row))

    return pieces

parse_fen("rnbqkbnr/pppp1ppp/8/8/8/8/PPPPPPPP/RNBQKBNR")


def generate_moves(board):
    raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")
