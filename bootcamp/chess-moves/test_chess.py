import chess


def test_opening_moves():
    board = chess.parse_fen(
        "rnbqkb1r/pppppppp/8/8/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 1"
    )

    moves = chess.generate_moves(board)
    assert len(moves) == 20, f"Expected 20 moves, but got {len(moves)}"


def test_zukertort_1():
    board = chess.parse_fen(
        "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1"
    )

    moves = chess.generate_moves(board)
    assert len(moves) == 20, f"Expected 20 moves, but got {len(moves)}"


def test_zukertort_2():
    board = chess.parse_fen(
        "rnbqkbnr/pppp1ppp/4p3/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2"
    )

    moves = chess.generate_moves(board)
    assert len(moves) == 23, f"Expected 23 moves, but got {len(moves)}"