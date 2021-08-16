import pandas as pd

df1 = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])
df2 = df1
print(df1)
df = pd.concat([df1, df2])
print(df)
df = pd.read_excel("showpd.xlsx")
print(df)
print(df.sort_values("Type", ascending=False))
print(df.head(10))
print(len(df))
