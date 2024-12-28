import numpy as np
import matplotlib.pyplot as plt
import sympy as smp

def newton_raphson(f, df, x0, max_iter=10):
    x = x0
    xs = [x]
    for _ in range(max_iter):
        x = x - f(x) / df(x)
        xs.append(x)
    return xs

x = smp.symbols('x')
f_sym = x**3 - 2*x**2 - x + 2
df_sym = f_sym.diff(x)

f = smp.lambdify(x, f_sym)
df = smp.lambdify(x, df_sym)

x0 = 3
xs = newton_raphson(f, df, x0)

x_plot = np.linspace(-2, 3, 1000)
y_plot = f(x_plot)

plt.figure(figsize=(12, 8))
plt.plot(x_plot, y_plot, 'b-', label='f(x)')
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')

for i in range(min(10, len(xs) - 1)):
    x1, x2 = xs[i], xs[i+1]
    y1, y2 = f(x1), f(x2)
    
    # Vertical line
    plt.plot([x1, x1], [0, y1], 'r--')
    
    # Tangent line
    m = df(x1)
    b = y1 - m * x1
    x_tangent = np.array([x1, x2])
    y_tangent = m * x_tangent + b
    plt.plot(x_tangent, y_tangent, 'g--')

plt.legend()
plt.title('Newton-Raphson Method Visualization')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

