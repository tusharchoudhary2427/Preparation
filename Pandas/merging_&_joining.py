import pandas as pd

# merging -> is used to combine two DataFrames based on common columns or indexes
# pd.merge(df1, df2, on = "Column_Name", how = "type_of_join")

df_customers = pd.DataFrame({
    'Customer_ID' : [1,2,3],
    'Customer_name' : ['Tushar', 'Rohit', 'Mohit'],
})

df_orders = pd.DataFrame({
    "Customer_ID" : [1,2,4],
    "Order_Amount" : [250, 333, 569]
})

# inner join
df1_mereged = pd.merge(df_customers, df_orders, on = 'Customer_ID', how= "inner")
print(df1_mereged)

# outer join
df2_mereged = pd.merge(df_customers, df_orders, on = 'Customer_ID', how= 'outer')
print(df2_mereged)

# left join
df3_merged = pd.merge(df_customers, df_orders, on = 'Customer_ID', how= 'left')
print(df3_merged)

# right join
df4_merged = pd.merge(df_customers, df_orders, on = 'Customer_ID', how= 'right')
print(df4_merged)

# cross join

df1 = pd.DataFrame({
    'Fruit': ['Apple', 'Banana']
    })
df2 = pd.DataFrame({
    'Color': ['Red', 'Green']
    })

df5_merged = pd.merge(df1, df2, how = 'cross')
print(df5_merged)