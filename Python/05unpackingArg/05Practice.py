def named(**kwargs): #packing named named arg into dict
    print(kwargs)
def details(**kwargs):
    named(**kwargs)#unpacking the keyword arg 
    # print(kwargs.items())
    for name,age in kwargs.items(): #destructing
        print(f"{name}:{age}")

details(name="Prashant",age=25)

#must be a dict for unpacking the arguments,else error will come
