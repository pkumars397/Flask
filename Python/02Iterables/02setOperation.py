friends={"ak","pk","sk"}
abroad={"ak","sk"}
local_friends=friends.difference(abroad)

allfriends=friends.union(abroad)
common=friends.intersection(abroad)
print(local_friends,allfriends,common)

# set() ,to create empty set,{} creates empty dict.
friend=['ak','pk']
ofriend=['ak','pk']
print(friend==ofriend) #True ,checks values only
print(friend is ofriend) #checks address also,checks if two objects are same or not