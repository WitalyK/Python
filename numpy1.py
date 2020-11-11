import numpy as np
from pprint import pprint

# nz = np.nonzero([1, 2, 0, 0, 4, 0])
# print(nz)

a = np.arange(14).reshape((2, 7))
#pprint(a)

# nz = np.hsplit(a, (3, 5))
# pprint(nz)

# nz = np.vsplit(a, 2)
# pprint(nz)

#nz = np.random.permutation(a)

Z = np.diag(np.arange(1, 5), k=2)
print(Z[0,0]==0)

# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(3 * 0.1)
# Z = np.zeros((8,8), dtype=int)
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1
# print(Z)
# Z = np.dot(np.ones((5,3)), np.ones((3,2)))
# print(Z)
# def generate():
#     for x in range(10):
#         yield x
# Z = np.fromiter(generate(),dtype=float,count=-1)
# pprint(Z)

# Z = np.arange(9).reshape(3,3)
# for index, value in np.ndenumerate(Z):
#     print(index, value)
# for index in np.ndindex(Z.shape):
#     print(index, Z[index])

# Z = np.random.randint(0,3,(3,10))
# print(Z)
# print((~Z.any(axis=0)).any())
# Z = np.arange(100).reshape(10, 10)
# v = np.random.uniform(0, 100)
# print(v)
# shape = (5, 5)
# position = (1, 1)
# P = np.array(list(position)).astype(int)
# pprint(P)
# Z = np.arange(100).reshape(10, 10)
# n = 3
# i = 1 + (Z.shape[0] - n)
# j = 1 + (Z.shape[1] - n)
# C = np.lib.stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
# pprint(Z.strides)
