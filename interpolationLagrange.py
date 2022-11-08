from tkinter import N
from numpy import zeros,array,dot,linspace
from random import randint
from math import pi, cos, sin


def interpolationLagrange(x, y, nb):
    Y=zeros(nb)
    X=linspace(-1,1,nb)
    for j in range(nb):
        Y=0
        n=len(x)
        for i in range(n):
            L=1
            for j in range(n):
                if(j!=i):
                    L*=(X-x[j])/(x[i]-x[j])
            Y+=y[i]*L
    return [X,Y]
