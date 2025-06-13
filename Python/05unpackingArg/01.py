def mul(*args):
    print(args) #*args pass the arguments as tuple
    return sum(args)
print(mul(1,2,4))

def add(x,y):
    return x+y
nums=[1,3]
print(add(*nums))