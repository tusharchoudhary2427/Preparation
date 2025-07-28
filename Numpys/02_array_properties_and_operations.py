# shape -> 

import numpy as np

arr_2d = np.array([[1,2,3],
                  [4,5,6]])
print(arr_2d.shape)

# size ->

filled_array = np.array([[7, 7], [4, 4]])
print(filled_array.size)

# no of dimension ->

array_1d = np.array([1,2,3])
array_2d = np.array([[7, 7, 7], [4, 4, 4]])
array_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])

print(array_1d.ndim)
print(array_2d.ndim)
print(array_3d.ndim)

# data type of element ->

arr = np.array([10, 20, 30.5, 40.5, 50, 60.5])
print(arr.dtype)

# to change datatype of element -> 

arr = np.array([10, 20, 30.5, 40.5, 50, 60.5])
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)

# mathematical operators -> 

arr = np.array([10,20,30,40])

print(arr + 3)
print(arr * 3)
print(arr ** 2)

# aggregations -> methods to summarize ndarray objects by applying various statistical operations on the array elements.

arr = np.array([3, 25,  7, 18, 11, 1, 21, 24, 16, 5])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))