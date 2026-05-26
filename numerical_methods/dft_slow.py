# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:13:51 2026

@author: arjun and yash
"""
import numpy as np
import matplotlib.pyplot as plt #Technically not needed
import random
# Custom for plotting multiple graphs
from grapher import plot_multiple_graphs
np.set_printoptions(suppress=True, precision=4)
#Sampling interval
sr  = 100
#Sampling rate
ts = 1/sr
def main():
    t = np.arange(0 , 1 + ts ,ts)
    x_net = random_sinusoids_noise(100 , t)
    N = len(x_net)
    freq_axis = [k * sr / N for k in range(N)]
    frequencies,magnitude = dft(x_net)
    plot_multiple_graphs((t , x_net ,'line','x(t)'),(freq_axis,magnitude,'stem','Magnitude of frequencies'))
"""
   Function for generating random sinusoids and returning
   their resultant wave
   Input - number of waves to generate , time array
   Output - Resultant wave
"""
def random_sinusoids(number_of_waves , time_vals):
    resultant_wave = 0
    for i in range(number_of_waves):
        amplitude = random.randint(1 , 5)
        freqeuncy = random.randint(2,6)
        resultant_wave += amplitude * np.sin(2 * np.pi * freqeuncy * time_vals)
    return resultant_wave
"""
   Functin for generatig random sinousoids with  white noise drawn
   from a normal distribution
"""
def random_sinusoids_noise(number_of_waves, time_vals):
    resultant_wave = 0
    for i in range(number_of_waves):
        amplitude = random.randint(1, 5)
        frequency = random.randint(2, 6)
        resultant_wave += amplitude * np.sin(2 * np.pi * frequency * time_vals)
    
    # Adding white noise cumsum takes the cumulative some
    noise = np.cumsum(np.random.normal(loc=0, scale=0.5, size=len(time_vals)))
    return resultant_wave + noise
#FUNCTION FOR COMPUTING NAIVE DFT
"""
   input - The signal of which the DFT is to be computed
   output - An array of containing computed X values and
   and array containing the magnitude 
"""
def dft(wave):
    #Technically this N - 1 due to how indexing works
    N = len(wave)
    X =[]
    for k in range(N):
        total = 0
        for n in range(N):
            value = (wave[n] * np.exp((-1j * 2 * np.pi * k * n)/N))
            total += value
        X.append(total)
    #Calculating the maginute of since the coefficients are 
    #... complex in nature(a +  ib)
    magnitude = []
    for i in range(len(X)):
        mags = abs(X[i])
        magnitude.append(mags)
    return X , magnitude
    
            
    
    
    
        
        
    
if __name__=="__main__":
    main()
    
    