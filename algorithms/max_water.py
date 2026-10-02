# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:54:44 2026

@author: arjun and yash
"""

def main():
    a = [1,8,6,2,5,4,8,3,7]
    pointer_l = 0
    pointer_r = len(a) - 1
    max_area = 0
    while pointer_l != pointer_r:
        area = abs((pointer_r - pointer_l) * min(a[pointer_r] ,a[pointer_l]))
        if max_area < area:
            max_area = area
        if a[pointer_l] <= a[pointer_r]:
            pointer_l +=1
        elif a[pointer_l] > a[pointer_r]:
            pointer_r -= 1
    print(max_area)
    


    
if __name__=="__main__":
    main()