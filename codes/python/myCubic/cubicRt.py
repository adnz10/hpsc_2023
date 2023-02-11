"""
A python module for calculating Cubic root using the Newton's method.
"""

def CubRT(x,debug=False,convergenceRate=False,zeroCase= True):
	"""
	x: the number whose cubic root is to be calculated
	convergenceRate: True to see convergence rate printed.
	"""
	from numpy import cbrt
	if zeroCase:
		if x==0.:
			return 0.
	assert x!=0., "Input not recognised"
	Guess=1.
	kmax=100
	ErrorLess= 1.e-16
	actual_value = cbrt(x)
	for k in range(kmax):
		if debug:
			print("At iteration number %s, value_iter= %20.15f" %(k,Guess))
		Guess= (1/3)*(2*Guess+x/Guess**2)
		dn = abs(Guess-actual_value)/abs(actual_value)
		if(abs(dn))<ErrorLess:
			break
		if convergenceRate:
			#Ignoring higher order terms, (Quadratic Convergence)
			dn = dn**2
			print("At iteration number %s, Convergence (error) = %20.15f" %(k,dn))
	if debug:
		print("After %s iterations, value_iter=%20.15f" %(k+1,Guess))
	return Guess

def test_main():
	import numpy as np
	xvalues1=[-1000,-64,-0., 8., 100, 1.e6]
	xvalues2=np.random.randint(1000,size=(1,100))
	xvalues = np.append(xvalues1,xvalues2)
	for x in xvalues:
		print("Testing with x=%20.15e" %x)
		Guess=CubRT(x)
		value_numpy=np.cbrt(x)
		print("CubRT guess = %20.15e, numpy value = %20.15e" %(Guess,value_numpy))
		assert abs(Guess-value_numpy) < 1e-14, "Your cubicRT does not agree with numpy cubicRT"
