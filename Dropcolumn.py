import pandas as pd
data={
    'student':["asa","aa","as","aww","aqq"],
    'rank':[2,4,5,8,7],
    'marks':[99,34,67,88,91]
}
a=pd.DataFrame(data)
print(a)
b=a.drop("rank",axis='columns')
print(b)
