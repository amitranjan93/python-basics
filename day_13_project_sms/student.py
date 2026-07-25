class Student:
    def __init__(self,roll_number, name, age, course, marks):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    
    def show(self):
        print('------------------------------------------')
        print(f"Roll Number : {self.roll_number}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Course      : {self.course}")
        print(f"Marks       : {float(self.marks)}")
        print('------------------------------------------')
