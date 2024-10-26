# [1]indexing using the indexing operator []

#import pandas as pd
#df=pd.read_csv("C:\\Users\\Admin\\Desktop\\ankita sonawane\\studentpeople.csv", index_col="Student")
#print("our dataframe=\n",df)
#res = df["Marks"]
#print("/n",res)

# [2] indexing using loc[]

#import pandas as pd
#df=pd.read_csv("C:\\Users\\Admin\\Desktop\\ankita sonawane\\studentpeople.csv", index_col="Student")
#print("our dataframe=\n",df)

#print("/n",df.loc["ankita"])


# [3] indexing using iloc[]

import pandas as pd
df=pd.read_csv("C:\\Users\\Admin\\Desktop\\ankita sonawane\\studentpeople.csv", index_col="Student")
print("our dataframe=\n",df)
res= df.iloc[2]
print("/n",res)



