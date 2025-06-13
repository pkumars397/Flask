class Student:
    def __init__(self,name,grades): #method inside class
        # self.name="Rolf"
        self.name=name
        self.grades=grades
    def average(self):
        return sum(self.grades)/len(self.grades)
student=Student("Prashant",(90,80,100))
print(student.name,student.grades,Student.average(student),student.average())