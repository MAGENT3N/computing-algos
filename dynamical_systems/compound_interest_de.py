# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:42:40 2026

@author: arjun and yash
"""

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from grapher import style_plot

def diff_eqn(t , u , p):
    du_dt = p * u
    return du_dt
def main():
    #Setting interest  rate to 100%
    p = 1.0/12.0
    #Setting initial amount to 1[initial condition]
    u = [1.0]
    #Solving for 1 year
    t_span = (0 , 12)
    #Creating a time array for smoother solution
    t_eval = np.linspace(0 , 12 , 12*365)
    solution = solve_ivp(diff_eqn, t_span,u ,args =( p,) ,t_eval=t_eval)
    """
       Setting up the plot
    """
    plt.figure()
    plt.plot(solution.t , solution.y[0])
    plt.x_label("Amount")
    plt.y_label("Time")
    plt.show()
if __name__=="__main__":
    main()