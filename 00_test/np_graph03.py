# グラフを試す (x-2)x(x+2)
import numpy as np
import matplotlib.pyplot as plt

def f2(x, w):
    return (x-w) * x * (x+2)

# x data
x = np.linspace(-3, 3, 100)  # -3 ~ 3  numver is 100

# graph normal
plt.plot(x, f2(x,2))
plt.show()

# graph
plt.plot(x, f2(x,2), color='black', label='$w=2$')
plt.plot(x, f2(x,1), color='blue' , label='$w=1$')
plt.legend(loc="upper left")
plt.ylim(-15,15)
plt.title("f_2(x)")
plt.show()

# graph
plt.plot(x, f2(x,2), color='black', label='$w=2$')
plt.plot(x, f2(x,1), color='blue' , label='$w=1$')
plt.legend(loc="upper left")
plt.ylim(-15,15)
plt.title("$f_2(x)$") # if you use $, it is tex format.
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.show()
