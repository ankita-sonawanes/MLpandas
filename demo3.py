import pandas as pd
da={
    'student':["asa","aa","as","aww","aqq","tt"],
    'rank':[2,4,5,8,7,8],
    'marks':[99,34,67,88,91,66]
}
df=pd.DataFrame(da,index=['RA','RB','RC','RD','RE','RF'],)
print("student record\n\n",df)
print("first 5 rows\n",df.head(5))