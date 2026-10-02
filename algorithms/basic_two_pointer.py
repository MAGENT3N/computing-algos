# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:32:33 2026

@author: arjun and yash
"""
"""
Input: s = "abc", t = "ahbgdc"
Output: true
"""
def main():
    s = "abc"
    t = "ahbgdc"
    # Converting the string to lists of the letters
    s = list(s)
    t = list(t)
    print(s)
    print(t)
    # Initializing the pointers
    pointer_s = 0
    pointer_t = 0
    # Setting the while loop
    while pointer_s < len(s) and pointer_t < len(t):
        # if element in s matches,we shift the pointer of s to the next element
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
        # we shift the pointer of t one unit after every iteration
        pointer_t += 1
    # if value of pointer_s is equal to the length s,this implies that
    #... every element of s has found a match in t as our if condition inside
    #... the while loop has been satisfied len(s) times
    if pointer_s == len(s):
        print("true")
    else:
        print("false")
    
                
            

    
    
    
if __name__=="__main__":
    main()