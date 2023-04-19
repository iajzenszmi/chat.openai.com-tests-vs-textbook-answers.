import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def kdv_equation(t, y, L):
    dy = np.zeros_like(y)
    dy[0] = 0
    dy[1:-1] = -0.5 * (y[:-2] - 2 * y[1:-1] + y[2:])
    dy[-1] = 0
    
    dyy = np.zeros_like(y)
    dyy[0] = 0
    dyy[-1] = 0
    dyy[1:-1] = 6 * y[1:-1] * dy[1:-1]

    return (1 / L**2) * dyy

def initial_condition(x, x0, c):
    return 0.5 * c * (np.cosh(0.5 * np.sqrt(c) * (x - x0))**(-2))

L = 100
N = 1000
x = np.linspace(-L, L, N)
x0 = 0
c = 1
y0 = initial_condition(x, x0, c)

t_eval = np.linspace(0, 10, 100)
sol = solve_ivp(kdv_equation, (0, 10), y0, t_eval=t_eval, args=(L,))

for i in range(len(t_eval)):
    plt.plot(x, sol.y[:, i])
    plt.ylim(-0.5, 2)
    plt.title(f"Soliton behavior at t = {t_eval[i]:.2f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.pause(0.1)
    if i < len(t_eval) - 1:
        plt.clf()

plt.show()

