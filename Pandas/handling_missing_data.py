import pandas as pd

data = {
    "Name" : ['Tushar', None, 'Rohan', 'Mohit', 'Aditya', 'Aryan'],
    "Age" : [24,None,22,25,29,20],
    "Salary": [64000, 38000, None, 45000, 70000, 48000],
    "Performance Score": [85,66,78,92,67,72]    
    }

df = pd.DataFrame(data)
print(df)

df['Age'].fillna(df['Age'].mean(), inplace = True)
print(df)

# interpolation -> It is used to fill in missing values (NaNs) in a DataFrame or Series by estimating values based on other data points. 

# 1 - preserve data integrity
# 2 - smooth trends
# 3 - avoid data loss

data1 = {
    "Name" : ['Tushar', 'Rohit', 'Rohan', 'Mohit', 'Aditya', 'Aryan'],
    "Age" : [24,None,22,25,29,20],
    "Salary": [64000, 38000, 55000, 45000, 70000, 48000],
    "Performance Score": [85,66,78,92,67,72]   
    }

df1 = pd.DataFrame(data1)
print(df1)

df1.interpolate(method='linear', axis=0, inplace=True)
print(df1)


#linear method

datatime = {
    "Time" : [1,2,3,4,5],
    "Value" : [10,None,30,None,50]
}

df = pd.DataFrame(datatime)
print('Before interpolation')
print(df)

df['Value'] = df['Value'].interpolate(method = 'linear')
print('After interpolation')
print(df)


# 1 - we can't use it with data related to categories (eg. names, id)
# 2 - it assumes a predictable pattern which might not be accurate or exist all the time.