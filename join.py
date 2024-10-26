import pandas as pd
data1={
    'id':["23","24","25","26","27"],
    'student':["ramit","amit","ankita","sona","saho"],
    'roll':[35,56,74,83,22]
}
data2={
    'rank':[1,4,3,6,7],
    'marks':[95,74,23,77,89]
}
dataFrame1=pd.DataFrame(data1)
print("dataframe 1=\n",dataFrame1)
dataFrame2=pd.DataFrame(data2)
print("dataframe 2=\n",dataFrame2)
resultantDF = dataFrame1.join(dataFrame2)
print("joining two dataframce\n",resultantDF)