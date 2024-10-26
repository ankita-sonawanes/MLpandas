#[1] select two columns
#import pandas as pd
#data = {
 #   'Student':["ankita","raj","pravin","kavita"],
  #  'Rank':["33","23","45","44"],
   # 'Marks':["1234","1256","5678","6789"]
#}
#df = pd.DataFrame(data)
#print("student recording\n",df)
#print("selecting only two columns:\n",df[['Rank','Marks']])

#[2] select multiple columns in a range
import pandas as pd
data = {
    'Student':["ankita","raj","pravin","kavita"],

    'Rank':[33,23,45,44],
    'Marks':[1234,1256,5678,6789],
    'Id':["a11","a12","a13","a14"],
    'Roll no':[102,345,233,121],
    'Address':["East","West","North","South"]
}
df = pd.DataFrame(data)
print("student recording\n",df)
print("selecting  columns:\n",df[df.columns[2:5]])