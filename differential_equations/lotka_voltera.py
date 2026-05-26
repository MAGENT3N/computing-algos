# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:19:51 2026

@author: arjun and yash
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lotka_voltera(t , u , alpha , beta , delta , gamma):
    # unpacking the initial conditions
    u1 , u2 = u  # u1 = x , u2 = y
    # Setting up the differential equations
    du1_dt = (alpha * u1) - (beta * u1 * u2)
    du2_dt = ( delta * u1 * u2 ) - (gamma * u2)
    return du1_dt , du2_dt
def main():
    # prey growth rate , pred-prey encounters , pred mortality rate,
    #... predator growth rate are the parameters
    alpha = 0.1
    beta = 0.02
    gamma = 0.4
    delta = 0.02
    u0 = [10 ,10]
    # Time till which we need to solve the equation
    t_span = (1 , 100)
    t_eval = np.linspace(1 , 100 ,10000)
    # Solving the system
    solution = solve_ivp(lotka_voltera
                         , t_span
                         ,u0 
                         ,args=(alpha , beta , delta , gamma)
                         ,t_eval=t_eval)
    # Adding constraints
    prey_values = solution.y[0]
    pred_values = solution.y[1]
    # Plotting the solution
    plot_solution(solution)
    plot_phase_potrait(solution)
    #mask = prey_values < 10
    # Analysis of the solution
    

    # # Plotting the points where these conditions are met
    # plt.plot(solution.t[mask], prey_values[mask], 'gx', label='Prey < 10')
    # plt.plot(solution.t[mask], pred_values[mask], 'rx', label='Pred when prey < 10')
    # plt.show()

    print(f"Prey values below 10   : {prey_values[prey_values < 10]}")
   # print(f"Pred values when prey < 10 : {pred_values[mask]}")
    # basic stats
    print(f"Max prey value     : {prey_values.max():.4f}")
    print(f"Max pred value     : {pred_values.max():.4f}")
    print(f"Min prey value     : {prey_values.min():.4f}")
    print(f"Min pred value     : {pred_values.min():.4f}")
    print(f"Average prey value : {prey_values.mean():.4f}")
    print(f"Average pred value : {pred_values.mean():.4f}")
    
    
# Helper functions for plotting    
def plot_solution(sol):
    plt.figure()
    plt.plot(sol.t ,sol.y[0],color = 'green',label = 'Prey')
    plt.plot(sol.t , sol.y[1],color = 'red', label = 'Predator')
    plt.xlabel("Time")
    plt.ylabel("Poplulation")
    plt.legend()
    plt.show()
def plot_phase_potrait(sol):
    plt.figure()
    plt.plot(sol.y[0] ,sol.y[1],color = 'pink')
    plt.xlabel("Prey Poplulation")
    plt.ylabel("Predator Population")
    plt.show()


    
if __name__=="__main__":
    main()
    
    