import pandas as pd

df = pd.read_excel("output.xlsx")

print('Display first 2 rows')
print(df.head(2))

print('Display last 2 rows')
print(df.tail(2))