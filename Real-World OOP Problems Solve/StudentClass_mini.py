class Student:
    def __init__(self, marks, grade):
        self._marks = marks
        self.grade = grade

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    
    def marks(self, value):
        if value < 0 or value > 100:
            raise ValueError("Marks must be Between")
        
        self._marks = value

        #pass / Fail message
            
        if value < 40:
            print("You are Fail")
        else:
            print("you Passed! Congo")

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,value):
        self._grade = value

print("--------------------------------------")
#calling
print("--------------------------------------")

student = Student(55, "7th")
print(student.marks)
print(student.grade)
student.marks = 30
student.marks = 80
