#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday 12 January 2021.

@author: h. thirtythreezero@outlook.com

References:
https://www.youtube.com/watch?v=et4tLWaINFY&ab_channel=purdueMET

"""
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# Libraries.
import matplotlib.pyplot as plt
import math
import random
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def obj_fnc():
    """
    """
    to_plot = []

    for x in list(range(0,200)):
        time_trav = (x/7.5) + ((math.sqrt(2500+((200-x)*(200-x))))/3)
        to_plot.append(time_trav)

        enter_water = to_plot.index(min(to_plot))

    print('HARDCODED ABSOLUTE VALUES:')
    print(f'The Lifeguard should enter the water at {enter_water}m down shore.')
    print(f'The Lifeguard will reach the swimmer in {min(to_plot):.2f}sec.')
    return to_plot, enter_water
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def monte_carlo_sim():
    """
    """
    rand_list = []
    sorted_rand_plot = []

    for i in list(range(0, 200)):
        n = random.randint(0,200)
        rand_list.append(n)

    sorted_rand_list = sorted(rand_list) # here we create randomised independant variable

    for x in sorted_rand_list: # here we plug independant to produced simulated dependant variables.
        time_trav = (x/7.5) + ((math.sqrt(2500+((200-x)*(200-x))))/3)
        sorted_rand_plot.append(time_trav)

        sim_enter_water = sorted_rand_plot.index(min(sorted_rand_plot))

    print('\nMONTE-CARLO SIMULATED VALUES:')
    print(f'The Lifeguard should enter the water at {sim_enter_water}m down shore.')
    print(f'The Lifeguard will reach the swimmer in {min(sorted_rand_plot):.2f}sec.')

    return sorted_rand_plot, sim_enter_water
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def plot_sim():
    """
    """
    data = obj_fnc()

    MCS = monte_carlo_sim()

    # Probability distribution of independant variable.
    plt.figure(1)
    plt.hist(list(range(0,200)), density=True, color='r')

    plt.title('Probability Distribution of Independent Variable')
    plt.xlabel('Distance to Enter Water (m)')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()

    # Uniform distribution of independant and dependant (MCS) variables.
    plt.figure(2)
    plt.plot(data[0], 'b', label='', zorder=10)
    plt.plot(data[1], min(data[0]), 'r+', markersize=12, \
             label=f'Optimum at {data[1]}m', zorder=20)

    for i in list(range(0,5)): # Run 5 Monte Carlo Simulations.
        MCS_i = monte_carlo_sim()
        plt.plot(MCS_i[0], '--',label=f'MCS SIM {i} at {MCS_i[1]}', zorder=0)

    plt.title('Lifeguard Problem for Monte Carlo Simulation')
    plt.xlabel('Distance to Enter Water (m)')
    plt.ylabel('Time to Reach Swimmer (s)')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

    # Histogram plot of dependant variable.
    plt.figure(3)
    plt.hist(data[0], density=True, bins=25, fill=True, color='r', \
             label='HAND CALC', zorder=0)
    plt.hist(MCS[0], density=True, bins=25, fill=False, color='b', \
             label='MCS SIM', zorder=10)

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
    plot_sim()
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
