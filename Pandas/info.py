# info -> gives a summary of your DataFrame — it tells you structure, column names, data types, non-null counts, and memory usage.

import pandas as pd

df = pd.read_json("output.json")

print('Displaying the info of the data set')
print(df.info())
