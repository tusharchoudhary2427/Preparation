# Not a Number -> It is used for missing or undefined numerical values.
import numpy as np
arr = ([10,20,30,np.nan,40,np.nan,60])

print(np.isnan(arr))

print(np.nan == np.nan) # we can't compare these because NaN is not equal to anything — not even itself.

# Replacing Missing Values with a Specific Value

arr = ([10,20,30,np.nan,40,np.nan,60])

cleaned_arr = np.nan_to_num(arr, nan = 69)
print(cleaned_arr)

# Replacing Missing Values with the Mean

arr = ([10,20,30,np.nan,40,np.nan,60])

mean_val = np.nanmean(arr)
arr_replaced = np.where(np.isnan(arr), mean_val, arr)
print(arr_replaced)

# Detect and Replacing Missing Values with infinite Value

arr = np.array ([1,2,np.inf,4,-np.inf,6])

print(np.isinf(arr))

# using positive and negative parameters to replace infinite values

arr = np.array([1, 2, np.inf, 4, -np.inf, 6, np.nan, 7])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf= 1000, neginf= -1000)
print(cleaned_arr)



