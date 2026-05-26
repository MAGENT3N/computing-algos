# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:15:30 2026

@author: arjun and yash
"""
"""
   FLOW:-
   1) x_data and y_data
   2) Minimizing least square error(cost function)
   3)for which we need the gradient of cost wrt
    ... w and b which are our paramteter
   4) Then we apply gradient descent which needs a step
      size(learning rate) and number of iterations and we also
      need to set the initial guess for w and b
"""
import matplotlib.pyplot as plt  
import random


def main():
    x_val ,y_val = generate_data(10)
    print(x_val,y_val)
    w,b = gradient_descent(x_val, y_val, learning_rate=0.001, iterations=10000)
    print(f"learned w:{w:.4f} learned b:{b:.4f}")
    print(f"equation of the line = {w:.3f}*x + {b:.3f}")
    

#    cost function
#   ... y = wx + b is the relationship that we are trying to model
def cost_function(x_val , y_val , w ,b):
    m = len(x_val)
    cost_sum = 0
    for i in range(m):
        f = w * x_val[i] + b
        #least square error
        cost = (f - y_val[i])**2
        cost_sum += cost
    total_cost = (1/(2*m)) * cost_sum
    return total_cost

#    gradient function
def gradient(x_val,y_val,w,b):
    m = len(x_val)
    partial_b = 0
    partial_w = 0
    for i in range(m):
        f = w * x_val[i]+b
        partial_w +=(f - y_val[i])*x_val[i]
        partial_b +=(f - y_val[i])
    partial_w = (1/m)*partial_w
    partial_b = (1/m)*partial_b
    return partial_w,partial_b
#   Gradient descent takes in the costfunction,learning rate
#... intial w and b and number of iterations

def gradient_descent(x_val , y_val ,learning_rate,iterations):
    # setting the paramenter to 0
    w = 0
    b = 0
    for i in range(iterations):
        dc_dw,dc_db = gradient(x_val,y_val,w,b)
        w = w - (learning_rate * dc_dw)
        b = b - (learning_rate * dc_db)
        print(f"for iteration {i} cost is : {cost_function(x_val,y_val,w,b)}")
    return w,b
  
        
        
    
#    generate data where the y-data has some noise   
def generate_data(data_points):
    x_data = [i for i in range(1,data_points + 1)]
    y_data = [round((3 * i)+ random.uniform(-1,1),3) for i in range(1 , data_points + 1)]
    return x_data , y_data
#   for plotting the scatter plot
def scatter_plot(x_val , y_val):
    plt.figure()
    plt.scatter(x_val , y_val)
    plt.show()

if __name__=="__main__":
    main()