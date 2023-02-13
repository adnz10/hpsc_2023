"""
A python module for calculating Cubic root using the Newton's method.
Code will run untill Convergence Rate is small.
"""
import numpy as np
def CubRT(x,debug=False,convergenceRate=False,zeroCase= True):
	"""
	x: the number whose cubic root is to be calculated
	debug: True if iteration details need to be printed. Default value is False
	convergenceRate: True to see convergence rate printed. Default value is False 
	"""
	if zeroCase:
		if x==0.:
			return 0.
	assert x!=0., "Input not recognised"
	Guess=1.
	kmax=100
	ErrorLessThan= 1.e-15
	actual_value = np.cbrt(x)
	for k in range(kmax):
		if debug:
			print("At iteration number %s, value_iter= %20.15f" %(k,Guess))
		Guess= (1/3)*(2*Guess+x/Guess**2)
		dn = abs(Guess-actual_value)/abs(actual_value)
		if convergenceRate:
			#Ignoring higher order terms, (Quadratic Convergence)
			CR = dn**2
			print("At iteration number %s, Convergence rate  = %20.15f" %(k,CR))
		if(abs(dn))<ErrorLessThan:
			break

	if debug:
		print("After %s iterations, value_iter=%20.15f" %(k+1,Guess))
	return Guess

def test_main():
	xvalues1=[-1000,-64,-0., 8., 100, 1.e6]
	xvalues2=np.random.randint(1000,size=(1,100))
	xvalues = np.append(xvalues1,xvalues2)
	for x in xvalues:
		print("Testing with x=%20.15e" %x)
		Guess=CubRT(x)
		value_numpy=np.cbrt(x)
		print("CubRT guess = %20.15e, numpy value = %20.15e" %(Guess,value_numpy))
		assert abs(Guess-value_numpy) < 1e-14, "Your cubicRT does not agree with numpy cubicRT"
