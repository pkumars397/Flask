users=[
    (0,"Bob","Password"),
    (1,"Prashant","p@ksjs")
]

userDetails={user[1]:user  for user in users}
print(userDetails)
#helpful in web Apps
user_name=input("Enter your name: ")
password=input("enter your password: ")

_,userName,Pass=userDetails[user_name]
if userName :
 if Pass==password:
    print("you good to go")
    
 else:
    print("Wrong password!")
else:
 print("You are not registered!")