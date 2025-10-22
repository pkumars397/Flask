#Series: It is defined as one dimensional array that is capable of holding any data type.
# It is similar to a list or a dictionary in Python.

import pandas as pd

# Creating a Series
x = [1, 2, 3, 4, 5]
data = pd.Series(x)

print(data)

print(type(data)) # Output: <class 'pandas.core.series.Series'>

print(data[2])


#can change index also
data = pd.Series(x, index=['a', 'b', 'c', 'd', 'e'],dtype='float',name='numbers')
print(data)

#series can be created from a dictionary
data_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
data_from_dict = pd.Series(data_dict)
print(data_from_dict,type(data_from_dict)) # Output: <class 'pandas.core.series.Series'>

#using int
s=pd.Series(12,index=[1,2,3,4,5])
print(s)
print(type(s)) # Output: <class 'pandas.core.series.Series'>

s2=pd.Series(13,index=[1,2,3,4],dtype='float')
print(s+s2)