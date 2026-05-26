# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:17:59 2026

@author: arjun and yash
"""
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def lorenz_system(t , u , sigma , rho , beta):
    # assigning the initial conditions to u
    x , y , z = u
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z ) - y
    dz_dt = (x * y) - ((beta) * z)
    return dx_dt,dy_dt,dz_dt

def main():
    # Assigning the constants for attractor
    sigma = 10
    rho = 28
    beta = 8/3
    #Time period for which we are solving the equations
    t_span = (1 , 100)
    # Creating time intervals for smooth solution
    t_eval = np.linspace(1 , 100 , 10000)
    # Initial conditions
    u0 = [1 , 1 ,1]
    #solution using solve_ivp
    solution = solve_ivp(lorenz_system, t_span, u0, args=(
        sigma , rho , beta),t_eval=t_eval)
    #Unpack the solution for smoother 3-d plotting
    # ..returns 4 arrays, 3 for each state and 1 for time
    x , y ,z = solution.y
    
    #Plotting the solutions in 3d space
    fig = plt.figure(figsize = (10 , 8))
    ax = fig.add_subplot(111 , projection = '3d')
    ax.plot(x , y , z , lw=0.5)
    ax.set_xlabel("X Phase Space")
    ax.set_ylabel("Y Phase space")
    ax.set_zlabel("Z Phase space")
    plt.show()
    
    

    
    
if __name__=="__main__":
    main()