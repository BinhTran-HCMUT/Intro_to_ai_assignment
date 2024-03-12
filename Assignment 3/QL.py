import numpy as np
import csv
import os
from copy import deepcopy
from state import State, UltimateTTT_Move

class QLearning():
    tag = 'O'
    values = dict()
    alpha = 0.5
    prev_stateStr = ""
    discount_factor = 0.9

    @staticmethod
    def make_move(state, winner):
        QLearning.state = state

        if winner is not None:
            new_state = state
            return new_state
        new_state = QLearning.make_optimal_move(state)
        return new_state


    
    @staticmethod
    def state2str(state):
        stateStr = ""
        for block in state.blocks:
            for row in block:
                for cell in row:
                    stateStr += 'X' if cell == 1 else 'O' if cell == -1 else '_'
        if state.previous_move is None:
            return "_"
        return stateStr
    @staticmethod
    def make_optimal_move(state):
        moves = state.get_valid_moves

        if len(moves) == 1:
            return moves[0]
        
        temp_state_list = []
        v = -float('Inf')
        v_temp = []
        for move in moves:            
            tempState = deepcopy(state)
            tempState.act_move(move)
            v_temp.append(QLearning.calc_value(QLearning.state2str(tempState)))
            # delets Nones
        v_temp = list(filter(None.__ne__, v_temp))
        if len(v_temp) != 0:
            v = np.max(v_temp)
        for moved in moves:
            tempState = deepcopy(state)
            tempState.act_move(moved)
            if QLearning.calc_value(QLearning.state2str(tempState)) == v:
                temp_state_list.append(moved)

        try:
            new_state = np.random.choice(temp_state_list)
        except ValueError:
            print('temp state:', temp_state_list)
            raise Exception('temp state empty')

        return new_state

    

    @staticmethod
    def reward(winner):
        if winner is QLearning.tag:
            return 1
        elif winner is None:
            return 0
        elif winner == 'DRAW':
            return 0.5
        return -1

    @staticmethod
    def learn_state(state, winner):
        stateStr = QLearning.state2str(state)
        if QLearning.tag in stateStr:
            if QLearning.prev_stateStr in QLearning.values.keys():
                prev = QLearning.values[QLearning.prev_stateStr]
            else:
                prev = int(0)

            R = QLearning.reward(winner)
            if R != 0:
                QLearning.values[stateStr] = R

            if stateStr in QLearning.values.keys() and winner is None:
                curr = QLearning.values[stateStr]
            else:
                curr = int(0)
            
            QLearning.values[QLearning.prev_stateStr] = prev + QLearning.alpha*(R + QLearning.discount_factor*curr - prev)
        QLearning.prev_stateStr = stateStr

    @staticmethod
    def calc_value(state):
        if state in QLearning.values.keys():
            return QLearning.values[state]
        return None

    @staticmethod
    def load_values():
        s = 'values' + QLearning.tag + '.csv'
        try:
            value_csv = csv.reader(open(s, 'r'))
            for row in value_csv:
                k, v = row
                QLearning.values[k] = float(v)
        except:
            pass

    @staticmethod
    def save_values():
        s = 'values' + QLearning.tag + '.csv'
        try:
            os.remove(s)
        except:
            pass
        a = csv.writer(open(s, 'a', newline=''))

        for v, k in QLearning.values.items():
            a.writerow([v, k])