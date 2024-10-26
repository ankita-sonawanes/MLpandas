import numpy as np
import pandas as pd
data=[33,56,78,11,33,np.nan]
s=pd.Series(data,name="ankita")
print("series:\n",s)
print("does the series has NaN?",s.hasnans)