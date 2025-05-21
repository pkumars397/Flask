l=['pk','bk','sk']
t=('pk','bk','sk')
s={'pk','bk','sk'}
# t[0]="ak" #error,can't add and remove from tuple
l.remove("pk")
l.append("pk")
print(l) 

s.add("ak")
print(s)