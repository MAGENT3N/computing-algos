# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:22:07 2026

@author: arjun and yash
"""
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from grapher import style_plot


# Setting up the Verhulst equation
def verhulst_eqn(t , N , r , k):
    dN_dt = (r * N) * (1 - (N/k))
    return dN_dt
    

def main():
    #Setting up the parameters
    r = 0.86
    k = 200
    #Setting up verhulst equation
    N0 = [1.0]
    #The time for which we will solve our de
    t_span = (1 , 10)
    #Creating a time array for a smooth solution
    t_eval = np.linspace(1 , 10 , 1000)
    #Solution of our ODE
    solution = solve_ivp(verhulst_eqn, t_span,N0 , args=(r , k) ,t_eval=t_eval)
    #Plotting our solution
    plt.figure(figsize=(10,8))
    plt.plot(solution.t, solution.y[0] )
    style_plot()
    plt.show()
    
    
    
if __name__=="__main__":
    main()