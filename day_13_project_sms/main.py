from student_manager import StudentManager

option = 0
manager = StudentManager()

while option != 10:
    print("========== Student Management System ==========")
    print("1. Add Student ")
    print("2. Search Student ")
    print("3. Delete Student ")
    print("4. Update Student ")
    print("5. Update Marks ")
    print("6. Show All Students ")
    print("7. Show Top Student ")
    print("8. Show Weak Student ")
    print("9. Show Class Average ")
    print("10. Exit ")
    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")
        continue
    if option < 1 or option > 10:
        print("Invalid Choice! Try Once Again!")
    elif option == 1:
        manager.add_student()
    elif option == 2:
        manager.search_student()
    elif option == 3:
        manager.delete_student()
    elif option == 4:
        manager.update_student()
    elif option == 5:
        manager.update_marks()
    elif option == 6:
        manager.show_all_students()
    elif option == 7:
        manager.top_student()
    elif option == 8:
        manager.weak_student()
    elif option == 9:
        manager.show_class_average()
    else:
        break
