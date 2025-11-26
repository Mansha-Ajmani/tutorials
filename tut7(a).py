# Q1
import numpy as np
A = np.array([[1,2],[3,4]])
print(A)
print(A[0])
print(A[:,1])

# Q2
B = np.arange(1,17).reshape(4,4)
print(B)
print(B[1:3, 1:3])
print(B[:, 2])
print(B[3])

# Q3
C = np.random.randint(10, 51, (5, 5))
print(C)
print(C[C > 30])

# Q4
D = np.array([[2,4],[6,8]])
print(np.linalg.det(D))
print(np.linalg.inv(D))

# Q5
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
import matplotlib.pyplot as plt
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Sin & Cos")
plt.show()

# Q6
t = np.linspace(0, 4*np.pi, 300)
x = t
y = np.sin(t)
plt.plot(x, y)
plt.title("Trajectory")
plt.show()

# Q7
u = np.random.randint(1, 51, 50)
print(u.mean(), u.std(), np.median(u))

# Q8
M = np.array([[2,1],[5,7]])
vals, vecs = np.linalg.eig(M)
print(vals)
print(vecs)
