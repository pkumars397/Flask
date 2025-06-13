class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self): #to turn object into string
        return f"{self.name} of age {self.age}"
    
    def __repr__(self):
        return f"<Person({self.name},{self.age})>"
bob=Person("Bob",35)
print(bob) #it will print string object.