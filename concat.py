import pandas as pd
data1={
    'id':["28r","25r","44r","55r","67"],
    'student':["amit","ankit","ankita","raj","pravin"],
    'roll':[101,203,456,56,22]
}
data2={
    'id':["28r","25r","44r"],
    'student':["arohi","ram","pravinya"],
    'roll':[101,203,456]
}
dataframe1=pd.DataFrame(data1,index=["student1","student2","student3","student4","student5"])

print("dataframe1=\n",dataframe1)
dataframe2=pd.DataFrame(data2,index=["student6","student7","student8",])
print("dataframe=2\n",dataframe2)
resDF=pd.concat([dataframe1,dataframe2])
print("concatenating dataframes=\n",resDF)

