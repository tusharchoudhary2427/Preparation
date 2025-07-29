import pandas as pd

# concatenation -> It is used to combine multiple DataFrames along a particular axis.
# pd.concat([df1, df2, axis =0, ignore_index = True])

df_region1 =pd.DataFrame({
    'Customer_ID' : [1,2,3],
    'Name' : ['Tushar', 'Rohit', 'Mohit']
})

df_region2 = pd.DataFrame({
    'Customer_ID' : [4,5,6],
    'Name' : ['Varun', 'Amit','Mayank']
})

df_concat1 = pd.concat([df_region1, df_region2], axis=0, ignore_index= True) # vertically
print(df_concat1)

df_concat2 = pd.concat([df_region1, df_region2], axis = 1, ignore_index= True) # horizontally
print(df_concat2)


# Ques -> You have two data frames, and you can use the merge method on both data frames to observe the relationship those data frames have with the customer id. From that point, you can provide a new DataFrame for each customer from these two data frames through concatenation using the pandas function.

import pandas as pd

df_customers = pd.DataFrame({
    'Customer_ID': [1, 2, 3],
    'Name': ['Tushar', 'Rohit', 'Mohit'],
})

# Transaction history
df_transactions = pd.DataFrame({
    'Customer_ID': [1, 2, 3],
    'Transaction_Amount': [5000, 7000, 6000],
})

df_mereged = pd.merge(df_customers, df_transactions, on= 'Customer_ID', how = 'inner')
print(df_mereged)

new_customer = pd.DataFrame({
    'Customer_ID': [4],
    'Name': ['Amit'],
    'Transaction_Amount': [8000],
})

concat_df = pd.concat([df_mereged, new_customer], axis = 0, ignore_index= True)
print(concat_df)

