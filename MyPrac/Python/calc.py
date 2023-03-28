import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = x**2

# plt.plot(x,y,'-r')
# plt.xlabel('X')
# plt.show()

a =np.array([[1,2],[2,3]])

print( np.linalg.eig(a))

c = 2**52
print(c)
print(f"value of c is {c}")
print("value of c is %20.11e " %(c))

list = [1,2,3,4]
print(2 in list)