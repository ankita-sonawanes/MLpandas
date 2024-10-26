import pandas as pd
data=[33,56,78,11,33]
s=pd.Series(data,index=["num1","num2","num3","num4","num5",], name="ankita")


print("series:\n",s)
print("series index\n",s.info())


