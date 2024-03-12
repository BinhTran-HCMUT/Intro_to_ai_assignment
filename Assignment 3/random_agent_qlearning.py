
from copy import deepcopy
import numpy as np
from QL import QLearning
from state import State_2, UltimateTTT_Move, State

choice = 2
def select_move(cur_state, remain_time, winner = None):
    # Play using QLearning
    if (choice == 1):
        valid_moves = cur_state.get_valid_moves
        if len(valid_moves) != 0:
            return QLearning.make_move(cur_state, winner)
        return None
    

    # Playing using last choice agent
    elif (choice == 2):
        valid_moves = cur_state.get_valid_moves
        if len(valid_moves) != 0:
            temp_state = deepcopy(cur_state)
            temp_state.act_move(valid_moves[len(valid_moves)-1])
            QLearning.learn_state(temp_state, winner)
            return valid_moves[len(valid_moves)-1]
        QLearning.learn_state(cur_state, winner)
        return None
    
    # Playing using random agent
    elif (choice == 3):
        valid_moves = cur_state.get_valid_moves
        if len(valid_moves) != 0:
            temp_state = deepcopy(cur_state)
            temp_state.act_move(np.random.choice(valid_moves))
            QLearning.learn_state(temp_state, winner)
            return np.random.choice(valid_moves)
        QLearning.learn_state(cur_state, winner)
        return None