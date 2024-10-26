import pandas as pd
data={
    'ID':["a01","a02","a03","a04","a05"],
    'student':["ankita","raj","sona","monu","tonu"],
    'Rank':[1,5,2,4,3],
    'Marks':[96,99,94,95,96]
}
a=pd.DataFrame(data)
print("student record\n",a)
#insert
#a.insert(2,"roll",[101,200,302,202,100])
#print("updated dataframe:\n",a)


# using assing()
resDf = a.assign(roll=[101,102,103,104,105])
print("updated dataframe:\n",resDf)