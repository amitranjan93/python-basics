## Today understood oops concept and worked on theory part rather than code

class Student:
    university = "Makaut University"
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print('===========Student Details==============')
        print(f"Student Name: {self.name}")
        print(f"Student Roll: {self.roll}")
        print(f"Student Marks: {self.marks}")
        print(f"Student University: {self.university}")
        
    @classmethod
    def change_university(cls,university):
        cls.university = university

    @staticmethod
    def is_pass(mark):
        return mark >= 40


student_1 = Student("Amit",10,90)
student_2 = Student("Rahul",11,50)
student_3 = Student("Amit",12,30)

student_1.display()
student_2.display()
student_3.display()

Student.change_university("Pune University")
print(Student.university)
student_3.display()

print(f"{student_1.name}: {'Pass' if Student.is_pass(student_1.marks) else 'Fail'}")
print(f"{student_3.name}: {'Pass' if Student.is_pass(student_3.marks) else 'Fail'}")