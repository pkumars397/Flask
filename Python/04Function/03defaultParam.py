def sum(x,y=5):
    print(x+y)
sum(1) 

# default parameter should come at end.first normal param then default.same like positional  and keyword arg.

a=10
def test(default_param=a):
    return default_param
a=20
print(test) #will print 10 because default paramter value gets value when function defined not when function called.