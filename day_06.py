students = []
option = 0
def add_student():
    name = input("Write name of the student: ")
    age = int(input("Write age of the student: "))
    mark = int(input("Write mark of the student: "))
    city = input("Write city of the student: ")
    students.append({"name":name,"age":age,"mark":mark,"city":city})
    print("Student Added Successfully!")

def show_all_students():
    if not students:
        print("No Student present!")
    for student in students:
        print(f"{student['name']} | {student['age']} | {student['mark']} | {student['city']}")

def find_student(name):
    flag = 0
    for student in students:
        if student["name"] == name:
            flag=1
            print(f"Name : {student['name']}")
            print(f"Age : {student['age']}")
            print(f"Mark : {student['mark']}")
            print(f"City : {student['city']}")
            break
    if not flag:
        print("Student Not present")

def delete_student(name):
    flag = 0
    for student in students:
        if student["name"] == name:
            flag = 1
            students.remove(student)
            print("Student Deleted Successfully!")
            break
    if not flag:
        print("Student Not present")
    
while option != 5:
    print("========== Student Database ==========")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Find Student")
    print("4. Delete Student")
    print("5. Exit")
    option = int(input("Enter your choice: "))
    if option < 1 or option > 5:
        print("Invalid Choice! Try Once Again!")
    elif option == 1:
        add_student()
    elif option == 2:
        show_all_students()
    elif option == 3:
        student = input("Write Name of the Student: ")
        find_student(student)
    elif option == 4:
        student = input("Write Name of the Student: ")
        delete_student(student)
    else:
        break

