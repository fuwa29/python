# numpy
import numpy as np
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

y = np.array([1.0, 2.0, 3.0])
z = np.array([2.0, 4.0, 6.0])

print(y + z)
print(y - z)
print(y * z)
print(y / z)

# broadcast 
print("BroadCast")
print(x / 2)