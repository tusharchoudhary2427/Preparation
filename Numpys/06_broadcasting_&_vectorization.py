# broadcasting -> adjusts the shape of arrays when you're doing operations (like addition, subtraction, etc.) between arrays of different shapes, as long as the shapes are compatible.

# without using broadcasting
prices = [100,200,300]
discount = 10
discounted_price = []

for price in prices:
    final_price = price - (price * discount/100)
    discounted_price.append(final_price) # every loop round, we keep adding more discounted prices.

print(discounted_price)

# using broadcasting

import numpy as np

prices = np.array([100,200,300,400,500])
discount = 10
final_prices = prices - (prices * discount/100)

print(final_prices)

# broadcasting for single value

import numpy as np

arr = np.array([100,200,300,400])
result = arr * 2

print(result)

# broadcasting from 1d to 2d array

import numpy as np

matrix = np.array([[1,2,3], [4,5,6]])
vector = np.array([10,20,30])

result = matrix + vector

print(result)

# error throwing 

# import numpy as np

# arr1 = np.array([[1,2,3], [4,5,6]])
# arr2 = np.array([1,2])


# result = arr1 + arr2 
# print(result) # it will throw and error and to overcome this we have to reshape the array before execueting the result

# vectorization -> it means doing operations on entire arrays without using loops.

# list comprehension -> it is a short and clean way to create a list using a single line of code, instead of using multiple lines and a loop.

# without using it

numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

# using it

num = [1,2,3,4,5,6]
squares = [num * num for num in numbers] 
print(squares)

# fast vectorized way

import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

result = arr1 + arr2

print(result)

# vectorization for 2d array

import numpy as np

arr2d = np.array([[10,20,30],
                 [40,50,60]])

result = arr2d * 10

print(result)


