from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product



class TicTacToe():

    def __init__(self):
        """initialise the board"""
        
        # initialise state as an array
        self.state = np.zeros((3,3)).astype(int) # initialises the board position, can initialise to an array or matrix
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, self.state.shape[0]*self.state.shape[1] + 1)] # , can initialise to an array or matrix

        self.reset()


    def is_winning(self, curr_state):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        
        #  Player who gets a sum of 15 in any directions wins the game
        if (curr_state.diagonal().sum() == 15 or np.fliplr(curr_state).diagonal().sum() == 15 or 
           np.any([curr_state[i,:].sum() == 15 for i in [0,1,2]]) or np.any([curr_state[:,i].sum() == 15 for i in [0,1,2]])):
            return True
        else:
            return False        
    
    
    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up

        if self.is_winning(curr_state) == True:
            return True, 'Win'

        elif not np.isin(0,curr_state):
            return True, 'Tie'

        else:
            return False, 'Resume'


    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state.astype(int).flatten()) if val == 0]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state.astype(int).flatten() if val != 0]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]
        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""
        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)



    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        position = curr_action[0]
        x = int(np.floor((curr_action[0]) / 3))
        y = int((curr_action[0]) % 3)
        new_state =  curr_state.copy()
        new_state[x,y] = curr_action[1]
        return new_state
        
    def step(self, curr_state, curr_action):
        """Takes current state and action and returns the next state, reward and whether the state is terminal. Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        next_state = self.state_transition(curr_state, curr_action)
        # Check if the game has reached terminal state
        terminal_state, message = self.is_terminal(next_state)
        if terminal_state:
            # End the game with the reward
            if message == "Win":
                game_result = "Agent Won!"
                rewards = 10
            else:
                game_result = "It's a tie!"
                rewards = 0
            return (next_state, rewards, terminal_state, game_result)
        else:
            # generate random environment action
            _, env_actions = self.action_space(next_state)
            env_action = random.choice([action for action in env_actions])
            
            new_state = self.state_transition(next_state, env_action)
            
            terminal_state, message = self.is_terminal(new_state)
            
            if terminal_state:
                if message == "Win":
                    game_result = "Environment Won!"
                    rewards = -10
                else:
                    game_result = "It's a tie!"
                    rewards = 0
                    
            else:
                rewards = -1
                game_result = "Resume"
        return (new_state, rewards, terminal_state, game_result)


    def reset(self):
        return self.state
