# Q1
import numpy as np

A1 = np.arange(5, 26)
print(A1)

A2 = np.random.randint(10, 51, (3, 4))
print(A2)


# Q2
print(A1.shape, A1.size, A1.dtype)
print(A2.shape, A2.size, A2.dtype)


# Q3
Array1 = np.array([2, 4, 6, 8, 10])
Array2 = np.array([1, 3, 5, 7, 9])

print(Array1 + Array2)
print(Array1 - Array2)
print(Array1 * Array2)
print(Array1 / Array2)


# Q4
B = np.arange(1, 10).reshape(3, 3)
print(B * 5)


# Q5
C = np.arange(10, 26).reshape(4, 4)
print(C[1])
print(C[:, -1])

C[0] = 0
print(C)


# Q6
D = np.random.randint(20, 41, 10)
print(D)
print(D[D > 30])


# Q7
E = np.arange(11, 23)
E2 = E.reshape(3, 4)
print(E2)


# Q8
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)
print(A.T)


# Q9
F = np.random.randint(10, 61, 15)
print(F)
print(np.mean(F), np.median(F), np.std(F))


# Q10
A = np.array([[2, 1, 3],
              [0, 5, 6],
              [7, 8, 9]])

print(np.linalg.det(A))
print(np.linalg.inv(A))
vals, vecs = np.linalg.eig(A)
print(vals)
print(vecs)
