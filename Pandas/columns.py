import pandas as pd

data = {
    "Name" : ['Tushar', 'Rohit', 'Rohan', 'Mohit', 'Aditya', 'Aryan'],
    "Age" : [24,26,22,25,29,20],
    "Salary": [64000, 38000, 50000, 45000, 70000, 48000],
    "Performance Score": [85,66,78,92,67,72]    
    }

df = pd.DataFrame(data) 
print(df)

# using assignment method

df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert() method

df.insert(0, "Employee_ID", [10,20,30,40,50,60])
print(df)

# updating values

df.loc[0, 'Salary'] = 78000
print(df)

# updating multiple values

df['Salary'] = df['Salary'] * 1.05

print(df)

# removing columns

df.drop(columns= 'Bonus', inplace = True)
print(df)
