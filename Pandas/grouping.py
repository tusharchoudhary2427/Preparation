import pandas as pd


data = {
    "Name" : ['Tushar', 'Rohit', 'Rohan', 'Mohit', 'Aditya', 'Aryan'],
    "Age" : [24,26,22,26,24,20],
    "Salary": [64000, 38000, 50000, 45000, 70000, 48000],
    "Performance Score": [85,66,78,92,67,72]    
    }

df = pd.DataFrame(data)
print(df)

# using groupby on age

# grouped = df.groupby('Age')['Salary'].sum()

grouped = df.groupby(["Age", "Name"])["Salary"].sum()

print(grouped)