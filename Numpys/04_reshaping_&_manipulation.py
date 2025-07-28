# reshaping -> means changing the structure of an array without changing its data.

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
reshaped_arr2 = arr.reshape(1,-1)

print("original :", arr)
print("reshaped :", reshaped_arr)

# flattening array -> it is used when we want to convert multi-dimensional array into 1d array.

arr = np.array([[1,2,3],[4,5,6]])
flattened_arr = arr.flatten()

print("original :", arr)
print("flattened :", flattened_arr)

# ravel -> it is used to convert multi-dimensional array into 1d array.

arr = np.array([[1,2,3],[4,5,6]])
ravel_arr = arr.ravel()

print("original :", arr)
print("ravel :", ravel_arr)