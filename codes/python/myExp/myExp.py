""""
A Python module to calculate the exponential using Taylor Series
exp(x) = summation(n=1, n=n) {x^n-1/(n-1)!}
"""
from numpy import exp

def expCal(x,n=100,):
    """
    Actual Exponential function expCal()
    Inputs
    x: the number whose exp is to be calculated
    n: (default n=100) number of terms to calculate the value of function in taylor series.
    """

    sum = 0
    for k in range(1,n):
        sum = sum + x**(k-1) / factorial(k-1)

    print(f"error is equal to {exp(x)-sum}")
    return sum
    


def factorial(y):
    """
    Calculate factorial of input
    eg. y*(y-1)*(y-2)*(y-3).........(y-y)
    """
    factor = 1
    for i in range(1,y+1):
        factor = factor*i

    return factor


expCal(100)