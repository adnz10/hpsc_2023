
a = 1
print(id(1))
print(id(a))

b = 1
print(id(b))
b = 2
print(id(b))

print(type(a))

c = [1,2,3]
print(id(c))
print(id(c[0]))
print(id(c[1]))
print(id(c[1])-id(c[0]))
print(id(c[2])-id(c[1]))

d = [1.0,2.0,3.0]
print(type(d[0]))
print(id(d[1])-id(d[0]),type(d))

print(id(d))
d.append(10)
print(id(d))

y = 1
print(id(y))
y = y+1
print(id(y))

import sys
print(sys.path)

ar = [[1],[2]]
print(type(ar))

import numpy as np
ar2 = np.array([[1,2],[2,3]])
print(type(ar2))
print(ar2.size)
print(ar2[0][1])

mat = np.matrix([[1],[2]])
print(type(mat))
print(mat.size)
print(mat[0][0])
print(mat[0,0])

x1 = np.array([1 ,2 ,3])
x2 = np.array([[1],[1],[1]])
print(np.dot(x1,x2))
print(np.matmul(x1,x2.T))