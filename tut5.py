# Q1
import numpy as np
A = np.array([[2, 3], [4, 5]])
B = np.array([[1, 6], [7, 2]])
print(A + B)
print(A - B)
print(A @ B)

# Q2
v1 = np.array([2, 3, 4])
v2 = np.array([1, 0, 6])
print(np.dot(v1, v2))
print(np.cross(v1, v2))

# Q3
M = np.array([[3, 1], [2, 4]])
print(np.linalg.det(M))
print(np.linalg.inv(M))

# Q4
X = np.linspace(0, 10, 5)
Y = np.linspace(5, 25, 5)
print(X)
print(Y)

# Q5
P = np.arange(10, 31).reshape(7, 3)
print(P)
print(P[:, 1])
print(P[2:6])

# Q6
Z = np.random.randint(1, 51, 12)
print(Z)
print(Z.reshape(3, 4))

# Q7
A = np.array([[1, 2], [3, 4]])
vals, vecs = np.linalg.eig(A)
print(vals)
print(vecs)

# Q8
C = np.random.randint(1, 21, (4, 4))
print(C)
print(C.mean())
print(C.std())
print(C.mean(axis=0))
print(C.mean(axis=1))
