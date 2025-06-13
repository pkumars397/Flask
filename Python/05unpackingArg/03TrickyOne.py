def multiply(*args):
    total=1
    for arg in args:
        total*=arg
    return total

def apply(*args,operator):
    if operator=="+":
        return sum(args)
    elif operator=="*":
        return multiply(*args) #if we only pass args ,we are passing the tuple only,not the values,so destructuring is needed.
    else:
        print("Please enter valid operator!")
print(apply(1,2,3,4,operator="+")) #this is important that named argument after positional argument.

print(apply(1,2,3,4,operator="*"))