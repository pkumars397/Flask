class ClassTest:
    def instance_method(self): #normal method inside class when refering to the object of class
        print(f"Called instance method of {self}")

    @classmethod #when needed class 
    def class_method(cls):
        print(f"Called class method of {cls}")
    
    @staticmethod #just a normal function inside the class
    def static_method():
        print(f"Called static method")

test= ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()