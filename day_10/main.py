import os
import expense_manager
import file_manager
option = 0

file_manager.load_expenses(expense_manager.expenses)
while option != 6:
    print("========== Expense Tracker ==========")
    print("1. Add Expense ")
    print("2. Show Expenses ")
    print("3. Search Expense ")
    print("4. Delete Expense ")
    print("5. Show Total Expense ")
    print("6. Exit ")
    option = int(input("Enter your choice: "))
    if option < 1 or option > 6:
        print("Invalid Choice! Try Once Again!")
    elif option == 1:
        expense_manager.add_expense()
    elif option == 2:
        expense_manager.show_expenses()
    elif option == 3:
        expense_manager.search_expense()
    elif option == 4:
        expense_manager.delete_expense()
    elif option == 5:
        expense_manager.show_total_expense()
    else:
        break