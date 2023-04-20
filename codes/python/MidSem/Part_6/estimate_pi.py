"""
Monte carlo method to estimate value of pi
"""
import numpy as np
import sys
def monte_carlo(num_points):
    if num_points <= 0:
        return 'Choose number greater than 0'
    count = 0
    for i in range(1,num_points+1):
        x = np.random.uniform(-0.5,0.5)
        y = np.random.uniform(-0.5,0.5)
        dist = np.sqrt(x**2+y**2)
        if dist <=0.5:
            count = count+1
        pi_cal = 4*count/num_points
    return pi_cal

def test_pi():
    from numpy import pi as pi_numpy
    xvalues = [10**2,10**3,10**4,10**5,10**6]
    for x in xvalues:
        print(f"Testing with pi = {x}")
        pi_cal = monte_carlo(x)
        print(f"pi_montecarlo = {pi_cal}, numpy pi = {pi_numpy}")
        assert abs(pi_cal-pi_numpy)/pi_numpy < 0.2, "Your pi monteCarlo doesnot agree"

if __name__ == "__main__":
    num_points = int(sys.argv[1])
    print(monte_carlo(num_points))

