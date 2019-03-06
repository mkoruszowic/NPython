# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:29:37 2018

@author: student
"""
import math, matplotlib.pyplot as plt

def f(n):
    x=[i*0.1 for i in range (n) ]
    y=[math.sin(x[i])**2+math.cos(x[i]) for i in range(n)]
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.suptitle('Wykres')
    plt.show()
    
n=int(input("Podaj dlugosc wykresu"))
f(n)