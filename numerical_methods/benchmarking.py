# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:22:09 2026

@author: arjun and yash
"""
import numpy as np
import timeit

def main():
    a = [x for x in range(10000)]
    b = [x**2 for x in range(10000)]
    c = []
    for i in range(len(a)):
        elem = a[i] + b[i]
        c.append(elem)

def vectorized_sum(a, b):
    a = np.array(a)
    b = np.array(b)
    c = a + b
    return c

if __name__ == "__main__":
    a = [x for x in range(10000)]
    b = [x**2 for x in range(10000)]

    t_loop = timeit.repeat(main, number=1, repeat=10)
    t_vec = timeit.repeat(lambda: vectorized_sum(a, b), number=1, repeat=10)

    print("loop:", np.mean(t_loop), min(t_loop))
    print("vectorized:", np.mean(t_vec), min(t_vec))
    