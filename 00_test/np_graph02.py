# グラフを試す (x-2)x(x+2)
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x-2) * x * (x+2)

# prepatre
print(f(1))
print(f(np.array([1,2,3])))

y = np.arange(-1, 3.5, 0.5)
print(y)

x = np.linspace(-3, 3, 10)  # -3 ~ 3  numver is 10
print(np.round(x,1))
print(np.round(x,2))
print(np.round(x,3))

# graph
plt.plot(x, f(x))
plt.show()
