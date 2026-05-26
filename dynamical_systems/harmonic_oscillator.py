# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:35:56 2026

@author: arjun and yash
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from grapher import style_plot

def harmonic_oscillator(t , u , k , m):
    # Defining the initial conditions
    # u1 is the position and u2 is the velocity and u is the state
    u1 , u2 = u
    du1_dt = u2 
    du2_dt = (-k/m) * u2
    return du1_dt,du2_dt
def main():
    # Physical parameters
    k = 1
    m = 1
    # Initial condition starting at 0 with unit velocity
    u0 = [0 , 1]
    # Time till which we calculate our solution
    t_span = (0 , 10)
    # Creating an array for smoother solution
    t_eval = np.linspace(0 , 10 , 1000)
    # Solving the differential equation
    solution = solve_ivp(harmonic_oscillator,
                         t_span, u0, args=( k , m) , t_eval=t_eval)
    plt.figure()
    # Time vs position graph
    plt.plot(solution.t , solution.y[0])
    plt.xlabel("Time")
    plt.ylabel("Position")
    style_plot()
    plt.show()
if __name__=="__main__":
    main()
              
    
    