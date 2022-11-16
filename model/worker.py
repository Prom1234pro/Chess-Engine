import chess
import random
import pickle
from ds import b_matrix

def games_and_outomes():
    all_board_states = []
    board = chess.Board()
    
    while not board.is_game_over():
        all_board_states.append(b_matrix(board))
        all_moves = list(board.legal_moves)
        random_move = random.choice(all_moves)
        w = board.turn
        board.push(random_move)
        if board.is_game_over():
            if board.is_checkmate():
                if w == chess.WHITE:
                    outcome = [1, 0, 0]
                if w == chess.BLACK:
                    outcome = [0, 1, 0]
            else:
                outcome = [0, 0, 1]
    return all_board_states, outcome


def save_games(file_name, no_of_games=1000):
    with open('data/' + file_name, 'wb') as fw:
        pickle.dump(generate_games(no_of_games), fw)

def load_data(file_name):
    with open('data/' + file_name, 'rb') as fw:
        file = pickle.load(fw)
        print(len(file))

def outcome_score_equator(outcome, a):
    if outcome[0] == 1:
        out = [0, 1, 0]
    elif outcome[1] == 1:
        out = [0, 0, 1]
    elif outcome[2] == 1:
        out = [0, 0.5, 0.5]
    return out[a]

def generate_games(n):
    nDArray = []
    for i in range(n):
        if(i % 5 == 0):
            print(i)
        board_states, outcome = games_and_outomes()
        a = 1
        for state in board_states:
            reward = outcome_score_equator(outcome, a)
            a *= -1
            st_re = {reward: state}
            nDArray.append(st_re)
    return nDArray
load_data("1_data.pgn")
