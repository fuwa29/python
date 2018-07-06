# numpy N次元配列
import numpy as np
a = np.array([[1,2],[3,4]])
print(a)

# 行列の形状
print(a.shape)

# 要素のデータ型
print(a.dtype)

b = np.array([[3,0],[0,6]])

print(a + b)
print(a * b)