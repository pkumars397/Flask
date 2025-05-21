friend_age={"Prashant":23,"Binu":26}
friend_age["Prashant"]=24
print(friend_age["Prashant"])

#Iteration,key can be of string and integer,also tuple.
#keys iteration
for name in friend_age:
    print(f"{name} age is {friend_age[name]}")

#items,dict.items returns ,list of key value tuple.
for name,age in friend_age.items():
    print(name,age)

if "Prashant" in friend_age:
    print("yess")    