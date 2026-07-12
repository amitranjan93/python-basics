expenses = []
option = 0
def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    date = input("Date in DD/MM/YYYY format: ")
    if not category:
        print("Category cannot be empty!")
    elif amount < 0:
        print("Amount cannot be negative")
    else:
        expenses.append({"category": category, "amount":amount, "date":date })
        print("Expense Added Successfully!")

def show_expenses():
    if not expenses:
        print("No Expenses available!")
    else:
        for expense in expenses:
            print(f"Category: {expense['category']}")
            print(f"Amount: {expense['amount']}")
            print(f"Date: {expense['date']}")
            print("--------------------------------------")

def search_expense():
    search_category = input("Enter Category: ")
    flag = False
    for expense in expenses:
        if expense["category"] == search_category:
            flag = True
            print(f"Category: {expense['category']}")
            print(f"Amount: {expense['amount']}")
            print(f"Date: {expense['date']}")
            print("--------------------------------------")
    if not flag:
        print("No Expense Found!")

def delete_expense():
    search_category = input("Enter Category: ")
    flag = False
    for expense in expenses[:]:
        if expense["category"] == search_category:
            expenses.remove(expense)
            flag = True

    if not flag:
        print("No Expense Found!")
    else:
        print("Expense(s) deleted successfully!")

def show_total_expense():
    total = 0
    if not expenses:
        print("No Expenses Available!")
    else:
        for expense in expenses:
            total+=expense["amount"]
        print(f"Total expense: {total:.2f}")

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
        add_expense()
    elif option == 2:
        show_expenses()
    elif option == 3:
        search_expense()
    elif option == 4:
        delete_expense()
    elif option == 5:
        show_total_expense()
    else:
        break