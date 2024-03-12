# from state import State
# from copy import deepcopy

import numpy as np

choice = 2
def select_move(cur_state, remain_time):
    # Playing using first choice agent
    if (choice == 1):
        valid_moves = cur_state.get_valid_moves
        if len(valid_moves) != 0:
            return valid_moves[0]
        return None
    
    # Playing using second choice agent
    elif (choice == 2):
        valid_moves = cur_state.get_valid_moves
        if len(valid_moves) != 0:
            if (len(valid_moves) >=2 ):
                return valid_moves[1]
            else: 
                return valid_moves[0]
        return None
    
    #Playing using random agent
    elif (choice == 3):
        valid_moves = cur_state.get_valid_moves
        if len(valid_moves) != 0:
            return np.random.choice(valid_moves)
        return None
