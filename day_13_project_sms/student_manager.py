from student import Student
import file_manager as fm

class StudentManager:
    def __init__(self):
        self.students = fm.load_students()

    def find_student_by_roll(self,roll_no):
        for curr_student in self.students:
            if roll_no == curr_student.roll_number:
                return curr_student
        return None

    def get_valid_integer(self,prompt, min_value, max_value):
        while True:
            try:
                number = int(input(f"Enter {prompt}: " ))
                if min_value <= number <= max_value:
                    return number
                else:
                    print(f"{prompt} must be in between {min_value} and {max_value}. Please try again.")
            except ValueError:

                print(f"{prompt} must be an integer. Please try again.")

    def get_valid_float(self,prompt, min_value, max_value):
        while True:
            try:
                number = float(input(f"Enter {prompt}: " ))
                if min_value <= number <= max_value:
                    return number
                else:
                    print(f"{prompt} must be in between {min_value} and {max_value}. Please try again.")
            except ValueError:
                print(f"{prompt} must be an valid number. Please try again.")
    

    def add_student(self):
        roll_no = self.get_valid_integer("Roll No",1,999999)
        student = self.find_student_by_roll(roll_no)
        if student:
            print("Student with this roll number already exists!")
            return
        name = input("Enter Name: ")
        age = self.get_valid_integer("Age",1,100)
        course = input("Enter Course: ")
        marks = self.get_valid_float("Marks",0,100)
        new_student = Student(roll_no,name,age,course,marks)
        self.students.append(new_student)
        fm.save_students(self.students)
        print("Student Added successfully!")

    def search_student(self):
        roll_no = self.get_valid_integer("Roll No",1,999999)
        student = self.find_student_by_roll(roll_no)
        if student:
            student.show()
            return
        print("No Student found with this roll number!")
        
    def delete_student(self):
        roll_no = self.get_valid_integer("Roll No",1,999999)
        student = self.find_student_by_roll(roll_no)
        if student:
            self.students.remove(student)
            fm.save_students(self.students)
            print("Student Removed Successfully!")
            return
        print("No Student found with this roll number!")
    
    def update_student(self):
        roll_no = self.get_valid_integer("Roll No",1,999999)
        student = self.find_student_by_roll(roll_no)
        if student:
            print("Current Student Details")
            student.show()
            student.name = input("Enter Name: ")
            student.age = self.get_valid_integer("Age",1,100)
            student.course = input("Enter Course: ")
            student.marks = self.get_valid_float("Marks",0,100)
            fm.save_students(self.students)
            print("Student Updated Successfully!")
            return
        print("No Student found with this roll number!")

    def update_marks(self):
        roll_no = self.get_valid_integer("Roll No",1,999999)
        student = self.find_student_by_roll(roll_no)
        if student is None:
            print("No Student found with this roll number!")
            return
        print(f"Student Current Mark: {student.marks}")
        mark = self.get_valid_float("Marks",0,100)
        student.marks = mark
        fm.save_students(self.students)
        print("Marks Updated Successfully!")
    
    def show_all_students(self):
        if not self.students:
            print("No Student Available!")
            return
        for student in self.students:
            student.show()
    
    def top_student(self):
        if not self.students:
            print("No Student Available!")
            return
        highest_mark = self.students[0].marks
        highest_mark_student = self.students[0]
        for student in self.students:
            if highest_mark < student.marks:
                highest_mark = student.marks
                highest_mark_student = student
        print("Top Student: ")
        highest_mark_student.show()

    def weak_student(self):
        if not self.students:
            print("No Student Available!")
            return
        lowest_mark = self.students[0].marks
        weak_student = self.students[0]
        for student in self.students:
            if lowest_mark > student.marks:
                lowest_mark = student.marks
                weak_student = student
        print("Weak Student: ")
        weak_student.show()
    
    def show_class_average(self):
        if not self.students:
            print("No Student Available!")
            return
        total_marks = 0
        for student in self.students:
            total_marks += student.marks
        average = total_marks/len(self.students)
        print(f"Average Marks of Class: {average:.2f}")


