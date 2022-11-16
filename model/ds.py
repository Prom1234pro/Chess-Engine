import numpy as np
import chess

squares_index = {
  'a': 0,
  'b': 1,
  'c': 2,
  'd': 3,
  'e': 4,
  'f': 5,
  'g': 6,
  'h': 7
}

def square_to_index(square):
  letter = chess.square_name(square)
  return 8 - int(letter[1]), squares_index[letter[0]]

# def init_board():
#     b = np.array([[[0 for _ in range(8)] for _ in range(8)] for _ in range(16)], dtype=np.float32)
#     return b
def attack_areas(board, square):
    return board.attacks(square=square).tolist()
    

def b_matrix(board):
    b_init = np.zeros((18,8,8))
    for piece in chess.PIECE_TYPES:
        for square in board.pieces(piece, chess.WHITE):
            index = np.unravel_index(square, (8, 8))
            b_init[piece - 1][7-index[0]][index[1]] = 1
        for square in board.pieces(piece, chess.BLACK):
            index = np.unravel_index(square, (8, 8))
            b_init[piece + 6][7 - index[0]][index[1]] = 1
        for square in board.pieces(piece, chess.WHITE):
            attacks = attack_areas(board, square)
            for s, attack in enumerate(attacks):
                index = np.unravel_index(s, (8, 8))
                if attack == True:
                    b_init[14][7-index[0]][index[1]] += 1
            b_init[14][:][:] /= 8
        for square in board.pieces(piece, chess.BLACK):
            attacks = attack_areas(board, square)
            for s, attack in enumerate(attacks):
                index = np.unravel_index(s, (8, 8))
                if attack == True:
                    b_init[15][7-index[0]][index[1]] += 1
            b_init[15][:][:] /= 8
            
    
    init_turn = board.turn
    board.turn = chess.WHITE
    board.turn = chess.WHITE
    for move in board.legal_moves:
        i, j = square_to_index(move.to_square)
        b_init[6][i][j] = 1
    board.turn = chess.BLACK
    for move in board.legal_moves:
        i, j = square_to_index(move.to_square)
        b_init[13][i][j] = 1
    board.turn = init_turn
    return b_init
# board  =  chess.Board()
# print(b_matrix(board))