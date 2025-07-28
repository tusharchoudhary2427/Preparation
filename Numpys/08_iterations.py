# iterations -> It means looping over array elements, so that we can go through it one by one.

import numpy as np

arr = np.array([9,8,7,6,5,4,3,2,1])
print(arr)

for i in arr:
    print(i)

# iterating over 2d array

arr_2d = np.array([[1,2,3,4], [5,6,7,8]])
print(arr_2d)

for i in arr_2d:
    print(arr_2d)

# # iterating over 2d array

arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_2d)

for i in arr_2d:
    for x in i:
       print(x)

# iterating over 3d/multidimensional array 

arr_3d = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(arr_3d.ndim)
print(arr_3d)

for i in arr_3d:
    for x in i:
       for y in x:
        print(y)

#  Using nditer() for Efficient Iteration

arr = np.array([[[1,2,3,4], [5,6,7,8]]])
print(arr)
print(arr.ndim)

for i in np.nditer(arr):  # flattens the array and it gives each element one by one, regardless of dimensions.
    print(i)

# Modifying Values While Iterating

arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr)

for i in np.nditer(arr, flags=['buffered'], op_dtypes="S"): # flags=['buffered'], Allow temporary conversion if needed and op_dtypes='S' convert each element to a byte string (like text) before using it
    print(i, i.dtype)
 
# To both index and value:

arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr)

for i,d in np.ndenumerate(arr):
   print(i,d)
