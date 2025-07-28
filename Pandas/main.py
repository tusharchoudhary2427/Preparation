import pandas as pd

data = {
    "Name" : ['Tushar', 'Rohit', 'Rohan', 'Mohit', 'Aditya', 'Aryan'],
    "Age" : [24,26,22,25,29,20],
    "Salary": [64000, 38000, 50000, 45000, 70000, 48000],
    "Performance Score": [85,66,78,92,67,72]    
    }

df = pd.DataFrame(data)
print('Sample DataFrame :')
print(df)

# selecting single columns

print(df["Name"])

# selecting multiple columns

subset = df[["Name", "Age", "Salary"]]
print(subset)

#  filtering rows 

high_salary = df[df['Salary'] >= 50000]
print(high_salary)

# filtering rows with multiple conditions using 'AND' condition

filtered_rows_using_and = df[(df['Age'] > 20) & (df['Salary'] > 50000)]
print(filtered_rows_using_and)

# filtering rows with multiplying conditions using 'OR' condition

filtered_row_using_or = df[(df['Age'] > 30) | (df['Performance Score'] > 80)]
print(filtered_row_using_or)