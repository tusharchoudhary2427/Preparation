# Describe -> is used to generate descriptive statistics of your DataFrame or Series — it gives you a quick summary of the numerical columns.

import pandas as pd

data = {
    "Name" : ['Tushar', 'Rohit', 'Rohan', 'Mohit', 'Aditya', 'Aryan'],
    "Age" : [24,26,22,25,29,20],
    "Salary": [64000, 38000, 50000, 45000, 70000, 48000],
    "Performance Score": [85,66,78,92,67,72]    
    }

df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print("Descriptive Statistics")
print(df.describe())