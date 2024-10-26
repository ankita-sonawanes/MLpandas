import pandas as pd
data ={
    'student':["ankita","pravin","raj","kavita","chaku"],
    'rank':[1,4,3,5,2],
    'marks':[99,67,89,12,33]
}
df=pd.DataFrame(data,index=['rowA','rowB','rowC','rowD','rowE'],)
print("student record\n\n",df)
print("no.of dimention:\n",df.ndim)