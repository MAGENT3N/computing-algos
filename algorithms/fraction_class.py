# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:40:35 2026

@author: arjun and yash
"""
# Fraction class
class fraction:
    def __init__(self , n , d):
        self.num = n
        self.den = d
    #Using __str__ for printing objects(in str type)
    def __str__(self):
        if self.den == 1:
            return f"{self.num}"
        return f"{self.num}/{self.den}"
    
    #Method for gettin the inverse
    def get_inverse(self):
        return self.den/self.num
    
    #Method for multiplying using dunder __mul__
    def __mul__(self,other):
        top = self.num * other.num
        bottom = self.den * other.den
        return fraction(top,bottom)
    #Method for casting fraction objects to floats
    def __float__(self):
        return self.num / self.den
    
        
def main():
    a = fraction(1, 2)
    print(a)
    b = fraction(3, 1)
    print(b)
    c = a * b
    print(c)
    print(float(c))
if __name__=="__main__":
    main()