marks = []
option = 0
def add_marks(new_mark):
    if  0 <= new_mark <=100:
        marks.append(new_mark)
        print("Mark Added Successfully!")
    else: 
        print("Invalid mark! Please enter a mark between 0 and 100.")

def show_marks():
    if len(marks) == 0:
        print("No Marks Available")
    else:
        print("All Marks:")
        for mark in marks:
            print(mark)

def show_average():
    if not len(marks):
        print("No Marks Available")
    else:
        total = 0
        for mark in marks:
            sum += mark
        average = total / len(marks)
        print(f"Average: {average:.2f}")

def show_highest_marks():
    if len(marks) == 0:
        print("No Marks Available")
    else:
        highest = marks[0]
        for mark in marks:
            if highest < mark:
                highest = mark
        print(f"Highest Mark: {highest}")

def show_lowest_marks():
    if len(marks) == 0:
        print("No Marks Available")
    else:    
        lowest = marks[0]
        for mark in marks:
            if lowest > mark:
                lowest = mark
        print(f"Lowest Mark: {lowest}")


while option != 6:
    print("========== Student Marks Manager ==========")
    print("1. Add Marks ")
    print("2. Show Marks ")
    print("3. Show Average ")
    print("4. Show Highest Marks ")
    print("5. Show Lowest Marks ")
    print("6. Exit")
    option = int(input("Choose an option: "))
    if  option < 1 or option > 6:
        print("Invalid Input Try Again!")
    elif option == 1:
        new_mark = int(input("Enter a mark: "))
        add_marks(new_mark)
    elif option == 2:
        show_marks()
    elif option == 3:    
        show_average()
    elif option == 4:
        show_highest_marks()
    elif option == 5:
        show_lowest_marks()
    elif option == 6:
        break

