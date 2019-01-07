# グラフを試す
import numpy as np
import matplotlib.pyplot as plt

# create data
np.random.seed(1)
x = np.arange(10)
y = np.random.rand(10)

print(x)
print(y)

# show graph
plt.plot(x, y)
plt.show()


