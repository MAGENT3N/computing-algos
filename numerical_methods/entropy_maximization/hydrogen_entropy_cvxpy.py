# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:49:36 2026

@author: arjun and yash
"""
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt



kT = 0.86 #eV for 10000 Kelving
kT_2 = 4.3 #eV for 50,000 Kelvin

def main():
    # Defining the energy levels of the hydrogen atom
    E_n = np.array([-13.6 , -3.4 ,-1.51 , -0.85 , -0.54 ])
    target,Z = target_energy(E_n)
    #Analytical Boltzmann
    p_boltzmann = np.exp(-E_n/kT_2)/Z
    print(target)
    #-----------------------------------------------------
    p = cp.Variable(5)
    # Our objective was to maximize log entropy which is concave so we can 
    # minimize the + log entropy which is the equivalent to that 
    objective = cp.Maximize(cp.sum(cp.entr(p)))
    constraints = [ cp.sum(p) == 1 , cp.sum(cp.multiply(p , E_n)) == target]
    problem = cp.Problem(objective , constraints)
    problem.solve()
    print(p.value)
    print(f"{problem.status} : {problem.value}")
    plot_results(p.value, p_boltzmann)
    
    
    
    
    
# Function for finding the target energy constraint
"""
    Parameter - A list of the energy levels
    Returns - Target Energy for T 10,000 K  and Z   

"""
def target_energy(E_n):
    # Value of kT for 10_000 K
    #Calculating the value of the partition 
    Z = np.sum(np.exp(-E_n / kT_2))
    average_energy = np.sum(np.exp((-E_n/kT_2))*(E_n)/Z)
    return average_energy , Z
"""
    Function for plotting
"""
def plot_results(p_optimization,p_analytical):
    n = np.arange(1, 6)
    width = 0.35
    plt.figure()
    plt.bar(n - width/2, p_optimization, width, label='cvxpy')
    plt.bar(n + width/2, p_analytical, width, label='Boltzmann')
    plt.xlabel('Energy level n')
    plt.ylabel('Probability')
    plt.title('Boltzmann distribution - Hydrogen at 10,000 K')
    plt.legend()
    plt.show()
    
    
    
if __name__=="__main__":
    main()