# Import routines

import numpy as np
import math
import random
from itertools import permutations

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [(0,0)] + list(permutations([i for i in range(m)], 2)) #List of all possible actions moving btwn locations
        self.state_space = [(X,T,D) for X in range(m) for T in range(t) for D in range(d)] #location, time of the day and day of the week 
         # The initial state is given by choosing random state from state space.
        self.state_init = random.choice(self.state_space)

        # Start the first round
        self.reset()


    ## Encoding state for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        # lets create encoded input for given state, value of 1 is 
        encod_state = [0] * (m + t + d)
        location, time, day = state
        encod_state[location] = 1
        encod_state[m + time] = 1
        encod_state[m + t + day] = 1
        return encod_state


    # Use this function if you are using architecture-2 
    # def state_encod_arch2(self, state, action):
    #     """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""

        
    #     return state_encod


    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 0:
            requests = np.random.poisson(2)
        elif location == 1:
            requests = np.random.poisson(12)
        elif location == 2:
            requests = np.random.poisson(4)
        elif location == 3:
            requests = np.random.poisson(7)
        elif location == 4:
            requests = np.random.poisson(8)

        #Lets cap requests to 15 if request crosses 15 
        if requests >15:
            requests =15

        posible_actions_index = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        actions_list = [self.action_space[i] for i in posible_actions_index]

        # lets Append the action (0,0) where the driver chose to remain idle.
        actions_list.append((0,0))
        posible_actions_index.append(0)
        return posible_actions_index,actions_list   

    def day_time_update_func(self, time, day, ride_duration):
        """Lets Takes current day of the week, current time of the day and ride_duration to return the updated time and day post ride."""
        ride_completed_day = (day + ((time + ride_duration) // t)) % d
        time_taken = (time + ride_duration) % t
        return time_taken, ride_completed_day


    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        
        #lets fetch the current location, time and day from the state
        current_loc, current_time, current_day = state
        pickup_loc, drop_loc = action
        
        #for idle state, lets multiply by -1
        if action == (0,0):
            reward = -1 * C
        
        else:
            # time time to reach pickup_loc from curr_loc 
            time1 = int(Time_matrix[current_loc][pickup_loc][current_time][current_day])
            current_time, current_day = self.day_time_update_func(current_time, current_day, time1)
            # time to reach drop_loc from pickup_loc 
            time2 = int(Time_matrix[pickup_loc][drop_loc][current_time][current_day])
            
            #lets calculate the reward for the ride
            reward = (R * time2) - (C * (time1 + time2))
        
        return reward


    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        current_loc, current_time, current_day = state
        pickup_loc, drop_loc = action
        
        rewards = self.reward_func(state, action, Time_matrix)
        total_time_taken = 0
        
        if action == (0,0):
            # for idle time, update the time by 1 hour
            current_time, current_day = self.day_time_update_func(current_time, current_day, 1)
            next_state = (current_loc, current_time, current_day)
            total_time_taken = 1
        else:
            # time from current_loc to reach pickup_loc
            time1 = int(Time_matrix[current_loc][pickup_loc][current_time][current_day])
            current_time, current_day = self.day_time_update_func(current_time, current_day, time1)
            
            # time from pickup_loc to reach drop_loc
            time2 = int(Time_matrix[pickup_loc][drop_loc][current_time][current_day])
            current_time, current_day = self.day_time_update_func(current_time, current_day, time2)
            
            #calculate the total time taken current location to drop location
            total_time_taken = time1 + time2
            next_state = (drop_loc, current_time, current_day)
        
        return next_state, rewards, total_time_taken


    def reset(self):
        return self.action_space, self.state_space, self.state_init
