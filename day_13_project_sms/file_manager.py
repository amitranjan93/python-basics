import os
from student import Student

def save_students(students):
    with open("day_13_project_sms/students.txt", "w") as file:
        for student in students:
            file.write(f"{student.roll_number}|{student.name}|{student.age}|{student.course}|{student.marks}\n")

def load_students():
    students = []
    if os.path.exists("day_13_project_sms/students.txt"):
        with open("day_13_project_sms/students.txt",'r') as file:
            for line in file:
                data = line.strip().split('|')
                students.append(Student(int(data[0]),data[1],int(data[2]),data[3],float(data[4])))
    else:
        file = open("day_13_project_sms/students.txt",'w')
        file.close()
    return students
