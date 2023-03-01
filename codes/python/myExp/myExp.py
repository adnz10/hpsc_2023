""""
A Python module to calculate the exponential using Taylor Series
exp(x) = summation(n=1, n=n) {x^n-1/(n-1)!}
Requirement:
Numpy Should be installed
Matplotlib Should be installed for Plotting Cmd
"""
import numpy as np

def expCal(x,n=100,convergence = False):
    """
    Exponential function expCalArray()
    Array Algorithm
    Inputs
    x: the number whose exp is to be calculated
    n: (default n=100) number of terms to calculate the value of function in taylor series.
    convergence: in order to print the convergence set convergence = True
    """
    assert n > 0, "Number of terms should be Positive and Not Eqaul to zero"
    x = np.array(x)
    n = n-1
    A = np.zeros((x.size,n+1))
    A[:,0] = 1
    low = range(1,n+1)
    high = range(n,0,-1)
    count = 0
    for k in np.nditer(x):
        k = int(k)
        for i,j in zip(low,high):
            A[count][i] = k**i/factorial(i)
            A[count][j] = k**j/factorial(j)
            if i>=j:
                break
        count = count+1

    result = np.sum(A,1)
    print(f"error is equal to {np.exp(x)-result}")
    if convergence:
         forward = A
         print(forward)
         backward = A
         forward = np.delete(forward,0)
         backward = np.delete(backward,-1)
         filter = forward - backward
         
    return result
    


def factorial(y):
    """
    Calculate factorial of input
    eg. y*(y-1)*(y-2)*(y-3).........(y-y)
    """
    assert y >= 0, "Factoriall is only defined for positive value"
    factor = 1
    for i in range(1,y+1):
        factor = factor*i
    return factor

def plotting():
        import matplotlib.pyplot as plt
        """
        To see plot between custom and numpy exponential function 
        """
        range = np.linspace(1,100,1000)
        myExpCal = expCal(range)
        numpyExpCal = np.exp(range)

        fig, ax = plt.subplots()
        ax.plot(range,numpyExpCal,label='Numpy Exp')
        ax.scatter(range,myExpCal,color='C1',label='Custom Exp')
        plt.legend()
        plt.show()
        
def test_main():
	xvalues=[0., 2., 6]
	for x in xvalues:
		print(f"Testing with x={x}")
		E = expCal(x)
		E_numpy= np.exp(x)
		print(f"myExp e^{x} = {E}, numpy e^{x} = {E_numpy}")
		assert abs(E-E_numpy) < 1, "Your myExp function does not agree with numpy exp function"

        
