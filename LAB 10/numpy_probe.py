import numpy as np
import random
import time
import math

nparray = np.array([1,2,3])
print(nparray)

nparray = np.array([[1,2,3],[4,5,6]])
print(nparray)

start = time.perf_counter()
print(np.sum(np.random.randint(0,1000,1000000)))
print(time.perf_counter() - start)

start = time.perf_counter()
print(sum(random.randint(0,1000) for _ in range(1000001)))
print(time.perf_counter() - start)

start = time.perf_counter()
print(math.fsum(random.randint(0,1000) for _ in range(1000001)))
print(time.perf_counter() - start)
