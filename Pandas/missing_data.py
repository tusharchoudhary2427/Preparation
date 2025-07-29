import pandas as pd

data = {
    "Name" : ['Tushar', None, 'Rohan', 'Mohit', None, 'Aryan'],
    "Age" : [24,None,22,25,None,20],
    "Salary": [64000, None, 50000, 45000, None, 48000],
    "Performance Score": [85,None,78,92,None,72]    
    }

df = pd.DataFrame(data)
print(df)

print(df.isnull())

print(df.isnull().sum())

# dropping a missing data

df.dropna(inplace = True)
print(df)

