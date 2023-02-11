"""
A python module for calculating square root using the 
Newton's method implemented in ME522 class
"""

def sqrtNT(x,debug=False,specialCases=True,convergenceRate=False):
	"""
	The actual sqrtNT function
	Inputs
	x: the number whose square root is to be calculated
	debug: True if iteration details need to be printed. Default value is False
	specialCases: False to disable zero and negative number check. Default value is True
	convergenceRate: True to see convergence rate printed.

	"""
	from numpy import nan
	from numpy import sqrt
	
	if specialCases:
		if x==0.:
			return 0.
		elif x<0.:
			print("An error has occured since you have passed a negative value for"
				"x which does not have a real square root")
			return nan
	assert x>0., "Input not recognised"	
	s=1.
	kmax=100
	tol=1.0e-14
	actual_value = sqrt(x)
	for k in range(kmax):
		if debug:
			print("At iteration number %s, s= %20.15f" %(k,s))
		s0=s
		s = 0.5*(s+x/s)
		delta_s=s-s0
		dn = abs(s-actual_value)/abs(actual_value)
		if(abs(delta_s/x))<tol:
			break
		if convergenceRate:
			#Ignoring higher order terms, (Quadratic Convergence)
			dn = dn**2/2 
			print("At iteration number %s, Convergence (error) = %20.15f" %(k,dn))
	if debug:
		print("After %s iterations,  s=%20.15f" %(k+1,s))
	return s

def test_main():
	from numpy import sqrt
	xvalues=[0., 2., 100, 1.e6]
	for x in xvalues:
		print("Testing with x=%20.15e" %x)
		s=sqrtNT(x)
		s_numpy=sqrt(x)
		print("sqrtNT s = %20.15e, numpy s = %20.15e" %(s,s_numpy))
		assert abs(s-s_numpy) < 1e-14, "Your sqrt does not agree with numpy sqrt"
