import pandas as pd
data1=[10,20,30,40,1000]
data2=[24,67,34,77,900]
series1=pd.Series(data1)
series2=pd.Series(data2)
print("series1:\n",series1)
print("series2:\n",series2)
def demo(x1,x2):
    if(x1 > x2):
        return x1
    else:
        return x2
res=series1.combine(series2,demo)
print("after combining\n",res)