friends=['Rolf','Bob',"Sk"]
print('Bob' in friends) #it works in list,tuple ,set,string.

#list Comprehension
friendWithS=[f for f in friends if f.startswith("S")]
print(friendWithS,id(friends),id(friends))