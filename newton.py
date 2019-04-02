import random
import math
#Newton-Rhapson Method:
#Xn+1 = Xn - f(Xn)/f'(Xn)

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

# def searchRange(f,a,b,t):
#     """Find an existing range for a root between a and b, using delta t, and returns c."""
#     if f(b) > 0 and f(a) < 0:
#         x1 = f(a)
#         x2 = f(b)
#     elif f(a) > 0 and f(b) < 0:
#         x1 = f(b)
#         x2 = f(a)
#     else:
#         print("\nSince f(a) and f(b) have the same sign, it can not be decided if Bolzano's theorem is valid.\n")
#         return False
#     #X1 < X2 (X1 NEGATIVE, X2 POSITIVE)
#     c = random.randint(a,b)
#     while not(f(c) <= (0.1) and f(c) >= (-0.1)):
#         x1 =
#     return c
