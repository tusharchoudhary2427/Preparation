# insert function -. 

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 2, 100,0)
print(new_arr)

# inserting in 2d array

arr_2d = np.array([[1,2], [3,4]])
print(arr_2d)

new_2d_arr = np.insert(arr_2d,1,[5,6],axis = 0)
print(new_2d_arr)

# append function -> adds elements at the end of the array. 

import numpy as np

arr = np.array([10,20,30])
new_app_arr = np.append(arr,[40,50,60,70])

print(new_app_arr)

# appending for 2d array

arr_2d = np.array([[10,20,30], [40,50,60]])
print(arr_2d)

new_app_arr = np.append(arr_2d,[70,80,90])
print(new_app_arr)

# joining 2 arrays

arr1 = ([10,20,30,40])
arr2 = ([50,60,70,80])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)

# joining 2 2d arrays

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])

new_res1 = np.concatenate((arr1, arr2),0)
new_res2 = np.concatenate((arr1, arr2), 1)
print(new_res1)
print(new_res2)

# deletion

arr = np.array([10,20,30,40,50])
print(arr)

new_arr = np.delete(arr,0)
print(new_arr)

# deletion for 2d array

arr_2d = np.array([[10,20],[30,40,],[50,60]])
print(arr_2d)

rows_arr2d = np.delete(arr_2d, 0, 0) # for rows
columns_arr2d = np.delete(arr_2d, 1, 1) # for columns
print(rows_arr2d, columns_arr2d)

#stacking

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])
arr3 = np.array([70,80,90])
print(arr1)
print(arr2)
print(arr3)
# stacking vertically
new_v_arr = np.vstack((arr1,arr2,arr3)) 
# stacking horizontally
new_h_arr = np.hstack((arr1,arr2,arr3))
print(new_v_arr)
print(new_h_arr)

# splitting arrays

arr = np.array([10,20,30,40,50,60])

print(np.split(arr,2))

# splitting for 2d array 

arr_2d = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(np.vsplit(arr_2d,3))
print(np.hsplit(arr_2d,3))

#  Modifying Values While Iterating 

arr = np.array([[1, 2, 3], [4, 5, 6]])
