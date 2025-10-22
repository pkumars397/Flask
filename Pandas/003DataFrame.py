import pandas as pd

l=[1, 2, 3, 4, 5]

var=pd.DataFrame(l)
print(var,type(var))


d={"a": [1, 2, 3, 4, 5], "b": [6, 7, 8, 9, 10], "c": [11, 12, 13, 14, 15]}
# var2=pd.DataFrame(d)
var2=pd.DataFrame(d,columns=["a"],index=[1, 2, 3, 4, 5])
print(var2,type(var2))

print(var2["a"][3])

#list of list 
l2=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var3=pd.DataFrame(l2)
print(var3,type(var3))

#frames using series
s1=pd.Series([1, 2, 3], index=["a", "b", "c"])
s2=pd.Series([4, 5, 6], index=["a", "b", "c"])
var4=pd.DataFrame({"s1": s1, "s2": s2})
print(var4,type(var4))