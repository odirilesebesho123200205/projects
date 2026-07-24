"""
FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

8  r n b q k b n r
7  p p p p p p p p
6  . . . . . . . .
5  . . . . . . . .
4  . . . . . . . .
3  . . . . . . . .
2  P P P P P P P P
1  R N B Q K B N R
   a b c d e f g h

when we take the FEN into parse_fen we get 
pieces = [
    [r n b q k b n r],  0   board[0][6] == piece "n"
    [p p p p p p p p],  1   piece_locations = [(0, 1), (0, 6)]
    [. . . . . . . .],  2
    [. . . . . . . .],  3
    [. . . . . . . .],  4
    [. . . . . . . .],  5
    [P P P P P P P P],  6
    [R N B Q K B N R],  7
]

"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
, to_move, castling_rights, ep, hm, fm 
"""

def main():
    """main function allows us to see code at the top of the file instead of the bottom"""

    board = parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    # print board as list
    print(board)
    print()

    # print the board
    display_board(board)
    print()

    print(generate_moves(board))
    print()

    # print(generate_moves(board))

def parse_fen(fen):
    """Takes a fen string and returns the board as a list of lists with all the pieces in it"""

    # split fen to get only the pieces section
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")

    board = [[]]

    # check every character in pieces section of fen string
    for char in fen_pieces:
        if char.isdigit(): # if a character is a digit 
            # we add "." * 8 to the last list/ row in the board
            board[-1].extend(["."] * int(char))

        elif char == "/":
            board.append([]) # add another list/ row
        else:
            board[-1].append(char) # add the piece to the list/ row

    return board

def generate_moves(board):
    """Returns the sum of all legal piece moves"""
    return (
         knight_moves(board) +
         king_moves(board) +
         rook_moves(board) + 
         bishop_moves(board) +
         queen_moves(board) +
         pawn_moves(board)
    )

# ======== PIECES FUNCTIONS ========
def knight_moves(board):
    """Returns number of legal moves a knight can make"""
    # stores all the positional moves were allowed to make
    moves = []

    # a knight can move in 8 directions one being 2 spaces and one up
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    # using a get_piece_locations we find all the places there are knights
    knight_locations = get_piece_locations("n", board)

    # check the row, column coordinates from the list of peices
    for row, column in knight_locations:
        for direction in directions:

            # use the direction in direction (row, column) to find the new location
            new_row = row + direction[0]
            new_column = column + direction[1]

            if is_on_board(new_row, new_column, board):
                if board[new_row][new_column] == ".":
                    moves.append((new_row, new_column))

    print(f"Knight moves: {moves}")           
    return len(moves)

def king_moves(board):
    """Returns the number of legal moves a king can make"""
    # stores all the positional moves were allowed to make
    moves = []

    # a knight can move in 8 directions one being 2 spaces and one up
    directions = [(1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (0, -1)]

    # using a get_piece_locations we find all the places there are knights
    king_locations = get_piece_locations("K", board)

    # check the row, column coordinates from the list of peices
    for row, column in king_locations:
        for direction in directions:

            # use the direction in direction (row, column) to find the new location
            new_row = row + direction[0]
            new_column = column + direction[1]

            if is_on_board(new_row, new_column, board):
                if board[new_row][new_column] == ".":
                    moves.append((new_row, new_column))

    print(f"King moves: {moves}")    
    return len(moves)

def rook_moves(board):
    """Returns the number of legal moves a rook can make"""
    moves = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rook_locations = get_piece_locations("R", board)

    for row, column in rook_locations:
        for direction in directions:

            # use the direction in direction (row, column) to find the new location
            new_row = row + direction[0]
            new_column = column + direction[1]

            while is_on_board(new_row, new_column, board) and board[new_row][new_column] == ".":
                moves.append((new_row, new_column))
                new_row = new_row + direction[0]
                new_column = new_column + direction[1]

    print(f"Rook moves: {moves}")   
    return len(moves)

def bishop_moves(board):
    """Returns the number of legal moves a bishop can make"""
    moves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    rook_locations = get_piece_locations("B", board)

    # I want to keep looping in the directions until i get stopped by a piece
    for row, column in rook_locations:
        for direction in directions:

            # use the direction in direction (row, column) to find the new location
            new_row = row + direction[0]
            new_column = column + direction[1]

            # Check if the new location is in the board and the new location is empty/ "."
            while is_on_board(new_row, new_column, board) and board[new_row][new_column] == ".":
                moves.append((new_row, new_column)) # add the new location to moves list

                # update the new location in the while loop until we hit a piece
                new_row = new_row + direction[0]
                new_column = new_column + direction[1]

    print(f"Bishop moves: {moves}")   
    return len(moves)

def queen_moves(board):
    """Returns the number of legal moves a queen can make"""
    moves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    rook_locations = get_piece_locations("Q", board)

    # I want to keep looping in the directions until i get stopped by a piece
    for row, column in rook_locations:
        for direction in directions:

            # use the direction in direction (row, column) to find the new location
            new_row = row + direction[0]
            new_column = column + direction[1]

            while is_on_board(new_row, new_column, board) and board[new_row][new_column] == ".":
                moves.append((new_row, new_column))
                new_row = new_row + direction[0]
                new_column = new_column + direction[1]

    print(f"Queen moves: {moves}")   
    return len(moves)

def pawn_moves(board):
    """Returns the number of legal moves a pawn can make"""

    moves = []
    directions = [(-1, 0)]
    pawn_locations = get_piece_locations("P", board)

    # I want to keep looping in the directions until i get stopped by a piece
    for row, column in pawn_locations:
        for direction in directions:
            # use the direction in direction (row, column) to find the new location
            new_row = row + direction[0]
            new_column = column + direction[1]

            # pawns can only move two squares so we keep moving forward until we hit a piece or 2 moves
            pawn_moves = 2
            while is_on_board(new_row, new_column, board) and board[new_row][new_column] == "." and pawn_moves > 0: 
                moves.append((new_row, new_column))
                new_row = new_row + direction[0]
                new_column = new_column + direction[1]

                # reduce the amount of moves the pawn can make
                pawn_moves -= 1


    print(f"Pawn moves: {moves}")   
    return len(moves)

# ======== APPLY MOVES ========
def apply_move(board, move):
    """Returns the an updated board based on move applied"""

    target_piece = move[0]

    # get the row and and column for the target piece
    piece_row = target_piece[0]
    piece_column = target_piece[1]


    target_square = move[1]
    # get the row and and column for the target piece
    piece_row = target_piece[0]
    piece_column = target_piece[1]

    # check if its a piece
    piece_row = target_piece[0]
    piece_column = target_piece[1]
    # if board[]
    pass

# ======== HELPER FUNCTIONS ========
def display_board(board):
    """Prints the chess board"""
    for row in board:
            print(" ".join(row))

def get_piece_locations(piece, board):
    """Return a list of all the locations of a piece type"""
    piece_locations = []

    # check each row inside of the board
    for row in range(len(board)):

        # check each column inside of the row
        for column in range(len(board[0])):

            # checks the specific coordinate and asks does it equal the piece we want
            if board[row][column] == piece:
                # add the (row, column) coordinate into piece locations
                piece_locations.append((row, column))

    # return the locations of all the pieces we were looking for
    return piece_locations

def is_on_board(row, column, board):
    """Determines whether a location is inside the board"""
    return 0 <= row < len(board[0]) and 0 <= column < len(board[0])

main()