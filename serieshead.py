
import pandas as pd
data=[33,56,78,11,33,3456,367,456,567]
s=pd.Series(data,name="ankita")
print("series:\n",s)
print("the first 5 rows of the series:\n",s.head(5))
print("the last 2 rows of the series:\n",s.tail(2))