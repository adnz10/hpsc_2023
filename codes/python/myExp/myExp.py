""""
A Python module to calculate the exponential using Taylor Series
exp(x) = summation(n=1, n=n) {x^n-1/(n-1)!}
"""
import numpy as np

def expCal(x,n=100,convergence = False,automatic = True):
    """
    Actual Exponential function expCal()
    Inputs
    x: the number whose exp is to be calculated
    n: (default n=100) number of terms to calculate the value of function in taylor series.
    convergence: to print convergence, set convergence to True.
    automatic: to get correct value, n will be changed in automatic mode.
    """

    divisionValue = 25
    if x > divisionValue:
        [multi, addi] = np.divmod(x,divisionValue)
        list1 = divisionValue*np.ones(multi)
        list1 = np.append(list1,addi)
    else:
        list1 = x

    result = 1
    for i in np.nditer(list1):
        i = int(i)
        sum = 0
        for k in range(1,n):
            sum = sum + i**(k-1) / factorial(k-1)
            if convergence and k > 1:
                conv = sum-sum2
                print(f"Convergence of series after n term ={k} is {conv}")
            sum2 = sum
        result = result*sum
        print(i)
        print(result)





    print(f"error is equal to {np.exp(x)-result}")
    return result
    


def factorial(y):
    """
    Calculate factorial of input
    eg. y*(y-1)*(y-2)*(y-3).........(y-y)
    """
    factor = 1
    for i in range(1,y+1):
        factor = factor*i
    return factor


expCal(30)
