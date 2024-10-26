
#import pandas as pd
#s=pd.Series(data: ["p", "s", "f", "h", "r"], dtype ="category")
#print ("series = \n",s)

import pandas as pd
s=pd.Series(["p","q","r","s"],dtype="category")
print("series=\n",s)
#append the category

s=s.cat.remove_categories("r")
#display the update category
print("\n updated categories\n",s)