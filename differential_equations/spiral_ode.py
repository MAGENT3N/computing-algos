# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:55:50 2026

@author: arjun and yash
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from grapher import style_plot
"""
   Function for setting up the ODE
   Input-time vector , state u which gets
   unpacked as the initial conditions, and coefficients
   Output - The ode system starting from the initial conditins u = [u1 , u2]
"""
def spiral(t , u , alpha , beta):
    # Assigning the initial conditions
    u1 , u2 = u 
    #Setting the differntial equation
    du1dt = ((-alpha) * (u1**3)) + ((beta) * (u2 **3))
    du2dt = ((-beta) * (u1**3)) + ((- alpha) * (u2 ** 3))
    return  du1dt , du2dt

def main():
    # Setting the parameter alpha and beta
    alpha = 0.1
    beta =  2.0
    # Time span for which we are solving
    t_span = (0 , 20)
    #creating time array for smoother solution
    t_eval = np.linspace(0 , 20 ,1000)  
    # The initla conditions which map to u1 and u2
    u0 = [1 , 1]
    # solving using solve_ivp
    solution = solve_ivp(spiral, t_span, u0, args=(alpha,beta),t_eval=t_eval)
    # Plotting the solutions in the time domain
    plt.figure()
    plt.plot(solution.t , solution.y[0],label = "u1")
    plt.plot(solution.t , solution.y[1], label = "u2")
    style_plot()
    plt.legend()
    # Plotting the phase potrait of the system
    plt.figure()
    plt.plot(solution.y[0],solution.y[1])
    plt.xlabel("u1")
    plt.ylabel("u2")
    style_plot(equal_aspect=True)
    plt.show()
        
    
    
    
    
    
if __name__=="__main__":
    main()