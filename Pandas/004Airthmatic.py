import pandas as pd

var =pd.DataFrame({"A":[1,2,3],"B":[3,4,5]})
# print(var)

var["C"]=var["A"]+var["B"]

print(var)

var["C"]=var["C"]*2
print(var)

var["Python"]=var["A"]>=2

print(var)

##Insert and delete
del var["C"]
var.pop("Python")
print(var)

var.insert(1,"D",var["A"]+var["B"])

print(var)