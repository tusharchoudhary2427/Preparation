# shape -> it is a method in Pandas is used to get the dimensions of a DataFrame or Series

import pandas as pd

data = {
    "Name" : ['Tushar', 'Rohit', 'Rohan', 'Mohit', 'Aditya', 'Aryan'],
    "Age" : [24,26,22,25,29,20],
    "Salary": [64000, 38000, 50000, 45000, 70000, 48000],
    "Performance Score": [85,66,78,92,67,72]    
    }

df = pd.DataFrame(data)

print(df)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')

