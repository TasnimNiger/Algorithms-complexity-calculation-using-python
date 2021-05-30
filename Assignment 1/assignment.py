# -*- coding: utf-8 -*-
"""
Created on Sun May 30 00:46:49 2021

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')

def Logarithmic(n):
    return np.log(n)

def Linear(n):
    return n

def Quadratic(n):
    return n*n

def Cubic(n):
    return n*n*n

def Polynomial(n,k):
    return n**k

#n=np.arange(0,7,1)
x=int(input("input item size:"))
n = np.linspace(1, 10, num=x)
k=int(input("input any positive value  to calculate polynomial:"))
#k=4
plt.figure(figsize=(10, 8))
plt.ylim(0, 50)
plt.plot(n, Logarithmic(n), c='red')
plt.plot(n, Linear(n), c='green')
plt.plot(n, Quadratic(n), c='blue')
plt.plot(n, Cubic(n), c='yellow')
plt.plot(n, Polynomial(n,k), c='black')
plt.xlabel('Size of input (n)', fontsize=16)
plt.ylabel('Run Time (y)', fontsize=16)
plt.legend(['$\mathcal{O}(\log n)$','$\mathcal{O}(n)$','$\mathcal{O}(n^2)$','$\mathcal{O}(n^3)$','$\mathcal{O}(n^k)$' ], loc = 'best', fontsize=13 );
plt.savefig('plot-complexity.png')