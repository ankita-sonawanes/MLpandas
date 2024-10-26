import pandas as pd
da={
    'student':["asa","aa","as","aww","aqq"],
    'rank':[2,4,5,8,7],
    'marks':[99,34,67,88,91]
}
df=pd.DataFrame(da,index=['RA','RB','RC','RD','RE'],)
print("student record\n\n",df)
print("no of element",df.size)
