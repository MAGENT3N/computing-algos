# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:14:03 2026

@author: arjun and yash
"""

import math
import random
import numpy as np
"""
    Program for taking arrays of data and calculating the covariance
    between them .Main task is to learn how to give arbitrary arguments
    to a function
"""
def main():
    arrays = generate_data(5, 10)
    for row in cov(*arrays):
        print([round(x,2) for x in row])
    
            
def generate_data(number_of_features, number_of_elements):
    """
        Description - Function for generating the data
        to generate the data points of whose covariance
        is to be calculated.
        
        Parameters - Number of features, number of elements in a feature
        
        Returns - Data arrays as a tuple, equal to the
        Number of features (*arrays)
    """
    arrays = []
    for i in range(number_of_features):
        arr = []
        for j in range(number_of_elements):
            arr.append(random.randint(1,10))
        arrays.append(arr)
    return arrays

    
def mean(array):
    """
           Description - Calculates the mean of an array
           
           Parameter   - An array
           
           Returns - The mean of the array
    """
    total = 0
    for i in range(len(array)):
        element_at_i = array[i]
        total += element_at_i
    average = round(total / len(array) , 4)
    return average


def cov(*args):
    """
         Descriptioin - Function for calculating the cova-
         riance matrix of the input features.
         
         Parameters - *args where args are the arrays of 
         the input features
         
         Returns - The covariance matrix of the arrays 
    """
    array = list(args)
    # Precomputing the mean of each feature
    means = [mean(elem) for elem in array]
    n = len(array)
    covariance = []
    for i in range(n):
        lst = []
        for j in range(n):
            total = 0
            for k in range(len(array[i])):
                total += round((array[i][k] - means[i]) * (array[j][k] - means[j]),4)
            lst.append(round(total/(len(array[i]) - 1),4))
        covariance.append(lst)
    return covariance
                


if __name__=="__main__":
    main()