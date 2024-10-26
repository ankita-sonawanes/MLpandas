import pandas as pd
df=pd.read_csv("C:\\Users\\Admin\\Desktop\\ankita sonawane\\studentpeople.csv")
print("our dataframe=\n",df)
print("top 5 rows=\n",df.head())
print("top 2 row=\n",df.head(2))

print("last 5 rows=\n",df.tail())
print("last 3 rows=\n",df.tail(3))

