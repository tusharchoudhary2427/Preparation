
python_list = [1,2,3,4,5,6,7,8,9]
print(python_list)

import numpy as np
numpy_array = np.array([1,2,3,4,5,6,7])
print(numpy_array)

# one dimensonal array -> 1D array 
numpy_array1 = np.array([1,2,3,4,5,6,7])
print(numpy_array)

# two dimensional array -> 2D array
numpy_array2 = np.array([[1,2,3],
                         [4,5,6],
                         [7,8,9]])
print(numpy_array2)

# multidimensional array -> 3D array

matrix = np.array([ [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]])

print(matrix)

# creating arrays with default

zeroes_array = np.zeros(3)
print(zeroes_array)

# creating arrays using ones

ones_array = np.ones((2,3))
print(ones_array)

# full fucntion

filled_array = np.full((2,2),7)
print(filled_array)

#creating sequence of numbers-> arange function arange function is similar to range function in python but it returns numpy array instead of python list
# arange function takes three parameters -> start, stop, step
# start is the starting point of the sequence
# stop is the end point of the sequence
# step is the difference between each number in the sequence

import numpy as np
arr = np.arange(1,11,2)
print(arr)

# identity matrices -> it is a sqaure matrix with ones on the diagonals and zero elsewhere.

import numpy as np
identity_matrix = np.eye(4)
print(identity_matrix)