import random
import math

def ex(x):
    return math.cos(x) - x**3

def aa(x):
    return x**x - 100

def derivative(f, x):
    """Derivative of f in x"""
    accuracy = 0.00000001
    deriv = (1.0/(2*accuracy))*(f(x+accuracy)-f(x-accuracy))
    return deriv

def newtonMethod(f,Xn,k):
    """Returns an approximate root of f, given a point Xn, with k turns"""
    Xn_1 = Xn - (f(Xn)/derivative(f,Xn))
    if k == 0:
        return Xn_1
    else:
        return newtonMethod(f,Xn_1,k-1)
