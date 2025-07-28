import pandas as pd

data = {
    "Name": ['Tushar', 'Rohit', 'Rohan'],
    "Age" : [24,26,22],
    "City" : ['Gurugram', 'Delhi', 'Noida']
}

df = pd.DataFrame(data)
print(df) 

# df.to_csv("output.csv", index = False)
# df.to_excel("output.xlsx", index = False)
df.to_json("output.json", index = False)