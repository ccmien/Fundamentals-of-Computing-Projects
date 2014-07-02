"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 5    # Number of trials to run
MCMATCH = 2.0  # Score for squares played by the machine player
MCOTHER = 3.0  # Score for squares played by the other player
  
# Add your functions here.
def mc_trial(board, player):
    ''' 
    This function takes a current board and the next player to move.
    '''
    next_player = player
    while(board.check_win() == None):        
        empty_len = len(board.get_empty_squares())
        next_move = board.get_empty_squares()[random.randrange(empty_len)]
        board.move(next_move[0], next_move[1], next_player)
        next_player = provided.switch_player(next_player)
            
def mc_update_scores(scores, board, player):
    '''
    This function takes a grid of scores (a list of lists) with the same dimensions as 
    the Tic-Tac-Toe board, a board from a completed game, 
    and which player the machine player is.
    '''
    if board.check_win() in [None, provided.DRAW]:
        return None
    if board.check_win() == player:
        matchscore = MCMATCH
        otherscore = -MCOTHER
    else:
        matchscore = -MCMATCH
        otherscore = MCOTHER
        
    for board_row in range(board.get_dim()):
        for board_col in range(board.get_dim()):
            if board.square(board_row, board_col) != provided.EMPTY:
                if board.square(board_row, board_col) == player:
                     scores[board_row][board_col] += matchscore
                else:
                     scores[board_row][board_col] += otherscore       

def get_best_move(board, scores):
    '''
    This function takes a current board and a grid of scores.
    '''
    if len(board.get_empty_squares()) == 0:
        return None
    high = scores[board.get_empty_squares()[0][0]][board.get_empty_squares()[0][1]]
    best_moves = []
    for pos in board.get_empty_squares():
        if scores[pos[0]][pos[1]] > high:
            high = scores[pos[0]][pos[1]]            
            best_moves = [pos]
        elif scores[pos[0]][pos[1]] == high:
            best_moves.append(pos)
    return best_moves[random.randrange(len(best_moves))]

def mc_move(board, player, trials):
    '''
     This function takes a current board, which player the machine player is, 
     and the number of trials to run.
    '''
    scores = [[0 for _col in range(board.get_dim())] for _row in range(board.get_dim())]  
    for _trial in range(trials):        
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)
    return get_best_move(board, scores)
    
# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
