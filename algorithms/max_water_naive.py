# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:50:00 2026

@author: arjun and yash
"""
"""
    GOAL: We have to maximize((y2-y1) * (x2-x1)) for all x,y pairs??
    y_i = a[i]
    x_i = i
    So we need to create index value pairs for each height location like
    (i , height[i]) then we can check for pair of pairs is the product maximizd
    
    

"""
import random
def main():
    a = [1,4,5,3,6,7,4]
    # we need to make the index value pairs
    x_y = []
    for index,value in enumerate(a):
        x_y.append((index,value))
    print(x_y)
    product = []
    for i in range(len(x_y)):
        for j in range(i + 1 , len(x_y)):
            x_loc = x_y[i][0] - x_y[j][0]
            y_loc = min(x_y[i][1],x_y[j][1])
            # y_loc = x_y[i ][1] - x_y[j][1]
            area = abs(x_loc * y_loc)
            product.append(area)
    print(product)
    print(max(product))
            
        
            
            
    
        
    
    
    
if __name__=="__main__":
    main()