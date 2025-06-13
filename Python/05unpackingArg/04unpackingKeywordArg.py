def named(**kwargs): #kwargs will collect named argument store into dict 
    print(kwargs)
named(name="Bob",age=24)

def named(name,age):
    print(name,age)

details={"name":"Prashant","age":25}
named(**details) #in func call to unpack the keyword arguments.
