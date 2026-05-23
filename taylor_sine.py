# -*- coding: utf-8 -*-
"""
Created on Fri May 22 09:38:47 2026

@author: arjun and yash
"""
# value of pi as a global variable
PI = 3.141592
def main():
    # User enters angle in degrees
    angle_in_degrees = float(input("Enter angle in degrees: "))
    # Converting radians to degrees
    angle_in_radians = angle_in_degrees * (PI / 180)
    sine_value = sin(angle_in_radians)
    print(f"The value of sin({angle_in_degrees}) is : {sine_value}")
# Function for calculating sine value at x using taylor series upto
#...4th order term        
def sin(x):
    sin_value = 0
    for i in range(0 , 5):
        sin_value += ((x**(2*i + 1))/factorial(2*i + 1)) * ((-1)**i)
    return round(sin_value , 4)

 # Function for calculating factorial of a number       
def factorial(n):
        
    if n == 1 or n == 0:
        return 1
    factorial_of_n = n * factorial(n-1)
    return factorial_of_n

if __name__=="__main__":
    main()