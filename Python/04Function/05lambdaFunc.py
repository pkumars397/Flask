add=lambda x,y:x+y #Anonymous function can also assign to some variable.
print(add(2,3))

#if you are not assigning to some name u have to use there itself.
(lambda x,y:x+y)(2,4)

#usecase of lamda func
l=[1,2,3]
doubled=[x*2 for x in l] #list comprehension
tripllled=[(lambda x:x*3)(x) for x in l] #bit unreadable
d=list(map(lambda x:x*2,l)) #same as list comprehension ,so less used.
print(doubled,tripllled,d)