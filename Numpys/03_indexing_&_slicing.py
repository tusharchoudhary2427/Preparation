# indexing -> we can access any single element at any position using this.

import numpy as np

arr = np.array([10,20,30,40])

print(arr[3])
print(arr[2])
print(arr[-1])

#Indexing in 2D Array

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[0],1)   
print(arr2d[1],2)   
print(arr2d[2],3)

# slicing -> it is used to extract the subset of the data.

import numpy as np

arr = np.array([20,40,60,80])

print(arr[1:3])
print(arr[::2])  
print(arr[::-1])

# fancy indexing -> it is used to access the array elements using the array of indices. Also it selects multiple elements at once.

import numpy as np

arr = np.array([10,30,50,70,90])

print(arr[[0,2,4]])

# fancy indexing in 2d array 

arr2d = np.array([[11, 12, 13],
                  [21, 22, 23],
                  [31, 32, 33]])


print(arr2d[[0, 2]])

# Get specific elements (row indices and column indices)
print(arr2d[[0, 1, 2], [2, 0, 1]])  

# Boolean masking -> lets you filter or select array elements based on a condition. 

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25])

# using multiple conditions

print(arr[(arr > 20) & (arr < 50)])

print(arr[(arr == 10) | (arr == 50)])

# boolean masking in 2D array

arr2d = np.array([[5, 10, 15],
                  [20, 25, 30],
                  [35, 40, 45]])


print(arr2d > 25)

