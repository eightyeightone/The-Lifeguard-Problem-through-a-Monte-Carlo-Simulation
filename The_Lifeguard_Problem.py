#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday 12 January 2021.
Finished on Friday 15 January 2021. Report to accompany on GitHub (thirythreezero).

@author: h.

References:
https://www.youtube.com/watch?v=et4tLWaINFY&ab_channel=purdueMET
"""
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
import matplotlib.pyplot as plt
import math
import random
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def time_trav():
    """
    Create a empty list of dependent variables (DV) to be assigned and plotted.
        Move through independent variables (IV)(inputs) and plug into function.
        Minimum time is the distance down the shore to enter water.
    """
    time_to_reach_swimmer = []
    dist_allowed_to_run = list(range(0,200)) # Bounds: can only run 0-200m down shore.

    for x_dist_shore in dist_allowed_to_run:
        # Total time func results the rate of change of time dependant on the
        # distance the lifeguard runs down the shore (enters the water).
        total_time_func = (x_dist_shore/7.5) + ((math.sqrt((50**2)+((200-x_dist_shore)**2)))/3)
        time_to_reach_swimmer.append(total_time_func)

        enter_water = time_to_reach_swimmer.index(min(time_to_reach_swimmer))

    print('HARDCODED ABSOLUTE VALUES:')
    print(f'The Lifeguard should enter the water at {enter_water}m down shore.')
    print(f'The Lifeguard will reach the swimmer in {min(time_to_reach_swimmer):.2f}sec.')
    return time_to_reach_swimmer, enter_water
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def MCS_time_trav():
    """
    Create empty lists to contain randomised IV.
        Generate randomised IV based on probability distribution (uniform)(histogram) and known bounds.
    Move through randomised IV plugging into time to save swimmer function.
        Output is DV (distance to enter water) at time it would take to reach swimmer.
        Minimum time is the distance down the shore to enter water.
    """
    rand_dist_shore = []
    MCS_time_to_reach_swimmer = []

    dist_allowed_to_run = list(range(0,200)) # Bounds: can only run 0-200m down shore.

    for x_dist_shore in dist_allowed_to_run:
        rand_dist_shore.append(random.randint(0,200)) # Rand based on uniform distribution.

    rand_dist_shore = sorted(rand_dist_shore)

    for x_dist_shore in rand_dist_shore:
        # Total time func results the rate of change of time dependant on the
        # distance the lifeguard runs down the shore (enters the water).
        total_time_func = (x_dist_shore/7.5) + (math.sqrt((50**2)+((200-x_dist_shore)**2))/3)
        MCS_time_to_reach_swimmer.append(total_time_func)

        MCS_enter_water = MCS_time_to_reach_swimmer.index(min(MCS_time_to_reach_swimmer))

    print('\nMONTE-CARLO SIMULATED VALUES:')
    print(f'The Lifeguard should enter the water at {MCS_enter_water}m down shore.')
    print(f'The Lifeguard will reach the swimmer in {min(MCS_time_to_reach_swimmer):.2f}sec.')

    return MCS_time_to_reach_swimmer, MCS_enter_water
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def plot_results():
    """
    3 Plots: (1)Probability distribution of independent variable (distance).
             (2)Uniform & MCS of time to reach swimmer vs distance to enter water.
             (3)Probability distribution of dependant variable (Uniform & MCS).
    """
    dist_allowed_to_run = list(range(0,200)) # Bounds: can only run 0-200m down shore.
    numb_MCS_simulations = list(range(0,5))

    time_travelled  = time_trav()
    MCS_time_travelled = MCS_time_trav()

    # PLOT 1.
    plt.figure(11)
    plt.hist(dist_allowed_to_run, density=True, color='r')

    plt.title('Probability Distribution of Independent Variable')
    plt.xlabel('Distance to Enter Water (m)')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()


    # PLOT 2.
    plt.figure(22)
    plt.plot(time_travelled[0], 'b', label='', zorder=10)
    plt.plot(time_travelled[1], min(time_travelled[0]), 'r+', markersize=12, \
             label=f'Optimum at {time_travelled[1]}m', zorder=20)

    for i in numb_MCS_simulations:
        MCS_i = MCS_time_trav()
        plt.plot(MCS_i[0], '--',label=f'MCS SIM {i} at {MCS_i[1]}m', zorder=0)

    plt.title('Lifeguard Problem for Monte Carlo Simulation')
    plt.xlabel('Distance to Enter Water (m)')
    plt.ylabel('Time to Reach Swimmer (s)')
    plt.legend()
    plt.grid(axis='y')
    plt.show()


    # PLOT 3.
    plt.figure(33)
    plt.hist(time_travelled[0], density=True, bins=25, fill=True, color='r', \
             label='HAND CALC', zorder=0)
    plt.hist(MCS_time_travelled[0], density=True, bins=25, fill=False, \
             color='b', label='MCS SIM', zorder=10)

    plt.title('Probability Distribution of Dependant Variable')
    plt.xlabel('Time to Reach Swimmer (s)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(axis='y')
    plt.show()
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
if __name__ == '__main__':
    """ What does this do?
    """
    plot_results()
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
