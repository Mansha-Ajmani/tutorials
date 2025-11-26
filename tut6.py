# Q1
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = 2 * x + 3
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = 2x + 3")
plt.show()

# Q2
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.show()

# Q3
x = np.linspace(0, 10, 100)
y = np.exp(-0.2 * x)
plt.plot(x, y)
plt.title("Exponential Decay")
plt.show()

# Q4
t = np.linspace(0, 2*np.pi, 200)
x = 5*np.cos(t)
y = 3*np.sin(t)
plt.plot(x, y)
plt.axis("equal")
plt.title("Ellipse")
plt.show()

# Q5
theta = np.linspace(0, 2*np.pi, 300)
x = np.cos(theta) * (1 + 0.5 * np.cos(8*theta))
y = np.sin(theta) * (1 + 0.5 * np.cos(8*theta))
plt.plot(x, y)
plt.axis("equal")
plt.title("Gear Profile")
plt.show()

# Q6
t = np.linspace(0, 20, 300)
x = t
y = np.sin(t)
plt.plot(x, y)
plt.title("Motion Profile")
plt.show()
