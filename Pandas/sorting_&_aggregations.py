import pandas as pd

# sorting data in 1 column

data = {
    "Name" : ['Tushar', 'Varun', 'Mohit'],
    "Age" : [23, 25, 20],
    "Salary" : [64000, 48000, 30000]
}

df = pd.DataFrame(data)

df.sort_values(by= "Age", ascending= True, inplace= True)
print('Sorted age by ascending')
print(df)

# sorting data in multiple columns

data1 = {
    "Name" : ['Tushar', 'Varun', 'Mohit', "Sourav", "Aryan", "Amit"],
    "Age" : [23, 25, 20, 30, 26, 24],
    "Salary" : [64000, 48000, 30000, 90000, 62000, 88000]
}

df1 = pd.DataFrame(data1)

df.sort_values(by = ["Age", "Salary"], ascending= [True, False], inplace= True )
print(df)

# Aggregation -> Aggregation means applying summary statistics (like sum, mean, count, etc.) to groups or entire datasets to reduce multiple values to a single value.

# sum ->
sum_salary = df['Salary'].sum()
print(sum_salary)

# avg -> 
avg_salary = df['Salary'].mean()
print(avg_salary)

# count
count_salary = df['Salary'].count()
print(count_salary)

#min
min_salary = df['Salary'].min()
print(min_salary)

#max
max_salary = df['Salary'].max()
print(max_salary)

#std
std_salary = df['Salary'].std()
print(std_salary)

#var
var_salary = df['Salary'].var()
print(var_salary)

#median
median_salary = df['Salary'].median()
print(median_salary)